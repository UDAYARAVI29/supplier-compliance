from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship
from database import Base

# Supplier model represents a supplier entity.
class Supplier(Base):
    __tablename__ = "suppliers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    contract_terms = Column(JSON, nullable=False)  # e.g. {"delivery_time": "within 7 days", ...}
    compliance_score = Column(Integer, nullable=False)
    last_audit = Column(Date, nullable=False)
    
    # One-to-many relationship with compliance records.
    compliance_records = relationship("ComplianceRecord", back_populates="supplier")


# ComplianceRecord model represents a compliance data record for a supplier.
class ComplianceRecord(Base):
    __tablename__ = "compliance_records"
    
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    metric = Column(String, nullable=False)  # e.g., "delivery time" or "quality"
    date_recorded = Column(Date, nullable=False)
    result = Column(String, nullable=False)   # could be numeric but stored as string for flexibility
    status = Column(String, nullable=False)     # e.g., "Compliant", "Non-compliant"
    
    supplier = relationship("Supplier", back_populates="compliance_records")
