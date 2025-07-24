# WingSpan

WingSpan is a Dockerized web application that allows users to upload, store, and visualize their personal flight history. It provides a web interface for uploading CSV files and displays cumulative flight paths on an interactive world map.

## ✈️ Features

- Upload flight history via CSV
- Store flight data in a PostgreSQL database
- View all uploaded flight routes on a map
- Supports both Mapbox GL JS and Leaflet.js for map rendering
- GeoJSON API for map overlays
- Built using FastAPI, PostgreSQL, and Docker

## 📂 Folder Structure

```
wingspan_app/
├── Dockerfile
├── docker-compose.yml
├── main.py
├── db.py
├── models.py
├── requirements.txt
├── .env
├── routes/
│   └── flights.py
├── static/
│   ├── upload.html          # CSV upload UI
│   ├── mapbox.html          # Map view using Mapbox GL JS
│   └── leaflet.html         # Map view using Leaflet.js
```

## 📋 CSV Upload

The CSV file must contain the following columns:

- `user_id`
- `airline`
- `flight_number`
- `origin`
- `destination`
- `distance_miles`
- `date` (format: `YYYY-MM-DD`)

Example row:
```
1,Delta,DL123,JFK,LAX,2475,2024-12-10
```

Upload via:  
📄 `/static/upload.html`

## 🌍 Map Interfaces

- **Mapbox**: `/static/mapbox.html`
  - Requires a [Mapbox access token](https://account.mapbox.com/access-tokens/)
- **Leaflet**: `/static/leaflet.html`
  - No key required, uses OpenStreetMap tiles

## 🚀 Getting Started

```bash
# Clone the repo and navigate into it
docker-compose up --build
```

Visit:
- `http://localhost:8000/static/upload.html` to upload CSV
- `http://localhost:8000/static/mapbox.html` to view flights (Mapbox)
- `http://localhost:8000/static/leaflet.html` to view flights (Leaflet)

## 📦 Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL with asyncpg
- SQLAlchemy + Databases
- Docker + Docker Compose
- Mapbox GL JS / Leaflet.js

## 📄 License

MIT License – feel free to use and modify!
