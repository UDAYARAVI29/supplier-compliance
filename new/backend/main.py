from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas, crud, utils
from datetime import datetime
import os
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Allow frontend (React) to communicate with the backend
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Create database tables (for development only; in production use Alembic)
models.Base.metadata.create_all(bind=engine)

#app = FastAPI(title="Supplier Compliance Monitor & Insights Dashboard")

# Dependency to get a DB session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Supplier Compliance Dashboard"}

# --- Static Routes (defined first to avoid routing conflicts) ---

# Endpoint to get AI-generated compliance insights based on all records.
@app.get("/suppliers/insights")
def get_insights(db: Session = Depends(get_db)):
    insights = crud.generate_insights(db)

    # Ensure insights is always a list
    if not isinstance(insights, list):
        insights = []  # Return an empty list if it's not an array

    return {"insights": insights}


# Bonus endpoint: Check weather impact on delivery compliance.
@app.post("/suppliers/check-weather-impact")
def check_weather_impact(request: schemas.WeatherImpactRequest, db: Session = Depends(get_db)):
    try:
        # Convert the delivery_date (assumed to be a date) to a Unix timestamp string.
        dt = datetime.combine(request.delivery_date, datetime.min.time())
        timestamp = str(int(dt.timestamp()))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid delivery_date: {e}")
    status = utils.fetch_weather_impact(request.latitude, request.longitude, timestamp)
    return {"supplier_id": request.supplier_id, "weather_status": status}

# --- CRUD Endpoints ---

# Endpoint to get all suppliers.
@app.get("/suppliers", response_model=list[schemas.Supplier])
def get_suppliers(db: Session = Depends(get_db)):
    return crud.get_all_suppliers(db)

# Endpoint to add a new supplier.
@app.post("/suppliers", response_model=schemas.Supplier)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db, supplier)

# Endpoint to get supplier details by ID.
@app.get("/suppliers/{supplier_id}", response_model=schemas.Supplier)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = crud.get_supplier_by_id(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

# Endpoint to upload compliance data and analyze using Gemini AI.
@app.post("/suppliers/check-compliance")
def check_compliance(record: schemas.ComplianceRecordCreate, db: Session = Depends(get_db)):
    new_record = crud.add_compliance_record(db, record)
    insights = utils.analyze_compliance_data(record.dict())
    return {"message": "Compliance record added", "insights": insights}

# --- Endpoints to Serve Excel Data ---

@app.get("/compliance-data")
def get_compliance_data():
    """
    Reads data from Task_Compliance_Records.xlsx and returns it as JSON.
    """
    # Absolute path to your Excel file.
    file_path = r"C:\Users\udayaravi\OneDrive\Desktop\new\data\Task_Compliance_Records.xlsx"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Compliance records file not found")
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {e}")
    return df.to_dict(orient="records")

@app.get("/supplier-overview")
def get_supplier_overview():
    """
    Reads data from Task_Supplier_Data.xlsx and returns it as JSON.
    """
    # Absolute path to your Excel file.
    file_path = r"C:\Users\udayaravi\OneDrive\Desktop\new\data\Task_Supplier_Data.xlsx"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Supplier data file not found")
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {e}")
    return df.to_dict(orient="records")
