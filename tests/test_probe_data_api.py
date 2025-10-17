import pytest
from utils.api_client import APIClient
import os

BASE_URL = "https://api.vehiclecloud.com/vnext"
API_KEY = os.getenv("VEHICLE_API_KEY", "your-api-key")

client = APIClient(BASE_URL, API_KEY)

@pytest.mark.probe
def test_probe_data_upload():
    """Simulate sending vehicle telemetry (Probe Data)"""
    payload = {
        "vehicleId": "VH12345",
        "latitude": 15.8497,
        "longitude": 74.4977,
        "speed": 42.5,
        "timestamp": "2025-10-17T10:00:00Z"
    }

    response = client.post("probe/upload", payload)

    assert response.status_code == 200
    assert response.json().get("message") == "Data uploaded successfully"
