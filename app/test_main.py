from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_shipment():
    payload = {
        "shipment_id": "SHP001",
        "origin": "Mumbai",
        "destination": "Delhi",
        "status": "In Transit"
    }
    response = client.post("/shipments/", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Shipment created successfully"

def test_get_shipment():
    # Test tracking the shipment
    response = client.get("/shipments/SHP001")
    assert response.status_code == 200
    assert response.json()["origin"] == "Mumbai"
    assert response.json()["destination"] == "Delhi"

def test_get_nonexistent_shipment():
    # Test how the app handles invalid IDs
    response = client.get("/shipments/INVALID_ID")
    assert response.status_code == 404
    assert response.json()["detail"] == "Shipment not found"