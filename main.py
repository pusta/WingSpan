from fastapi import FastAPI
from routes import flights

app = FastAPI(title="WingSpan Flight Tracker")

app.include_router(flights.router)


from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
