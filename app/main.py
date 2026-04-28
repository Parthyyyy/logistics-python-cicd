from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# notes to self :
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# .\venv\Scripts\activate to activate virtual environment
# to run : uvicorn app.main:app --reload

app = FastAPI(title="Logistics API", version="1.0.0")

shipments_db: Dict[str, dict] = {}

class Shipment(BaseModel):
    shipment_id: str
    origin: str
    destination: str
    status: str = "Pending"

@app.get("/health")
def health_check():
    """Kubernetes will use this to check if the pod is alive."""
    return {"status": "healthy"}

@app.post("/shipments/")
def create_shipment(shipment: Shipment):
    """Create a new shipment in the system."""
    if shipment.shipment_id in shipments_db:
        raise HTTPException(status_code=400, detail="Shipment ID already exists")
    
    shipments_db[shipment.shipment_id] = shipment.model_dump()
    return {"message": "Shipment created successfully", "shipment": shipments_db[shipment.shipment_id]}

@app.get("/shipments/{shipment_id}")
def get_shipment(shipment_id: str):
    """Track a shipment by its ID."""
    if shipment_id not in shipments_db:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    return shipments_db[shipment_id]