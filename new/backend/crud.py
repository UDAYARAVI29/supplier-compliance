import models
from sqlalchemy.orm import Session
from models import Supplier, ComplianceRecord
from schemas import SupplierCreate, ComplianceRecordCreate
from datetime import date

# Create a new supplier
def create_supplier(db: Session, supplier: SupplierCreate):
    db_supplier = Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

# Retrieve all suppliers
def get_all_suppliers(db: Session):
    return db.query(Supplier).all()

# Retrieve a supplier by ID
def get_supplier_by_id(db: Session, supplier_id: int):
    return db.query(Supplier).filter(Supplier.id == supplier_id).first()

# Add a compliance record
def add_compliance_record(db: Session, record: ComplianceRecordCreate):
    db_record = ComplianceRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# Dummy function to simulate OpenAI insights generation.
# In production, integrate with OpenAI API here.
def generate_insights(db: Session):
    try:
        records = db.query(models.ComplianceRecord).all()  # Ensure models is imported
        
        if not records:
            return ["No compliance records available."]
        
        insights = []
        for record in records:
            compliance_score = record.compliance_score
            supplier_id = record.supplier_id
            late_deliveries = record.late_deliveries
            weather_impact = record.weather_impact

            if compliance_score >= 90:
                insights.append(f"🏆 Supplier {supplier_id} has an excellent compliance score of {compliance_score}%.")
            elif compliance_score < 70:
                insights.append(f"⚠️ Supplier {supplier_id} has a low compliance score of {compliance_score}%.")
            else:
                insights.append(f"Supplier {supplier_id} has a compliance score of {compliance_score}%.")

            if late_deliveries > 3:
                insights.append(f"🚨 Supplier {supplier_id} had {late_deliveries} late deliveries recently.")

            if weather_impact:
                insights.append(f"⛈️ Weather delays affected Supplier {supplier_id}.")

        return insights

    except Exception as e:
        print(f"Error in generate_insights: {e}")  # Debugging
        return ["Error fetching insights."]
