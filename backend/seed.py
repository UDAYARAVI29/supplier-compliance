from datetime import date
from database import SessionLocal, engine
from models import Base, Supplier, ComplianceRecord

# Ensure tables exist (for development use only; in production, use migrations)
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    try:
        # Add sample suppliers
        supplier1 = Supplier(
            name="Supplier One",
            country="USA",
            contract_terms={"delivery_time": "within 7 days", "quality_standard": "ISO9001", "discount_rate": 5},
            compliance_score=84,
            last_audit=date(2024, 3, 29)
        )
        supplier2 = Supplier(
            name="Supplier Two",
            country="USA",
            contract_terms={"delivery_time": "within 7 days", "quality_standard": "ISO9001", "discount_rate": 5},
            compliance_score=60,
            last_audit=date(2023, 11, 12)
        )
        db.add_all([supplier1, supplier2])
        db.commit()

        # Add sample compliance records for supplier1
        record1 = ComplianceRecord(
            supplier_id=supplier1.id,
            metric="Delivery Time",
            date_recorded=date(2024, 8, 5),
            result="Fail",
            status="Non-compliant"
        )
        record2 = ComplianceRecord(
            supplier_id=supplier1.id,
            metric="Quality",
            date_recorded=date(2024, 8, 16),
            result="Fail",
            status="Pass"  # This is just sample data; adjust as needed.
        )
        db.add_all([record1, record2])
        db.commit()
        print("Database seeding completed successfully!")
    except Exception as e:
        db.rollback()
        print("Error during seeding:", e)
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
