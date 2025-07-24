from sqlalchemy import Table, Column, Integer, String, Float, Date, MetaData

metadata = MetaData()

flights = Table(
    "flights",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("airline", String),
    Column("flight_number", String),
    Column("origin", String),
    Column("destination", String),
    Column("distance_miles", Float),
    Column("date", Date),
)
