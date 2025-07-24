from fastapi import APIRouter
from db import database
from models import flights
import geojson
from sqlalchemy import select

router = APIRouter(prefix="/flights", tags=["flights"])

@router.on_event("startup")
async def startup():
    await database.connect()

@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@router.get("/geojson")
async def get_flight_paths():
    query = select(flights)
    results = await database.fetch_all(query)
    features = [
        geojson.Feature(
            geometry=geojson.LineString([(r["origin"], r["destination"])]),
            properties={k: v for k, v in r.items() if k not in ("origin", "destination")}
        ) for r in results
    ]
    return geojson.FeatureCollection(features)


from fastapi import File, UploadFile, HTTPException
import csv
import io
from datetime import datetime
from sqlalchemy import insert

@router.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only CSV files are allowed.")

    content = await file.read()
    decoded = content.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))

    required_fields = {"user_id", "airline", "flight_number", "origin", "destination", "distance_miles", "date"}
    if not required_fields.issubset(reader.fieldnames):
        raise HTTPException(status_code=400, detail=f"CSV must contain the following fields: {required_fields}")

    values = []
    for row in reader:
        try:
            values.append({
                "user_id": int(row["user_id"]),
                "airline": row["airline"],
                "flight_number": row["flight_number"],
                "origin": row["origin"],
                "destination": row["destination"],
                "distance_miles": float(row["distance_miles"]),
                "date": datetime.strptime(row["date"], "%Y-%m-%d").date(),
            })
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error parsing row: {row}, error: {str(e)}")

    query = insert(flights)
    await database.execute_many(query=query, values=values)

    return {"status": "success", "rows_inserted": len(values)}
