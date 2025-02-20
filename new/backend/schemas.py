from datetime import date
from typing import Optional, List, Any
from pydantic import BaseModel

# Pydantic schema for a Supplier
class SupplierBase(BaseModel):
    name: str
    country: str
    contract_terms: dict
    compliance_score: int
    last_audit: date

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True


# Pydantic schema for a ComplianceRecord
class ComplianceRecordBase(BaseModel):
    supplier_id: int
    metric: str
    date_recorded: date
    result: str
    status: str

class ComplianceRecordCreate(ComplianceRecordBase):
    pass

class ComplianceRecord(ComplianceRecordBase):
    id: int

    class Config:
        orm_mode = True


# Schema for Weather Impact Request (Bonus Feature)
class WeatherImpactRequest(BaseModel):
    supplier_id: int
    latitude: float
    longitude: float
    delivery_date: date


# Schema for responses from OpenAI or similar
class AIResponse(BaseModel):
    insights: str
