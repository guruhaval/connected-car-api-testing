import pytest
from utils.api_client import APIClient
import os

BASE_URL = "https://api.vehiclecloud.com/vnext"
API_KEY = os.getenv("VEHICLE_API_KEY", "your-api-key")

client = APIClient(BASE_URL, API_KEY)

@pytest.mark.fod
def test_fod_activation():
    """Verify Feature on Demand activation endpoint"""
    payload = {
        "vehicleId": "VH12345",
        "featureName": "heated_seat",
        "requestSource": "user_app"
    }
    response = client.post("fod/activate", payload)

    assert response.status_code == 200
    body = response.json()
    assert body.get("status") == "activated"
    assert "timestamp" in body
