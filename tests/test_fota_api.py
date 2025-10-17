import pytest
from utils.api_client import APIClient
import os

BASE_URL = "https://api.vehiclecloud.com/vnext"
API_KEY = os.getenv("VEHICLE_API_KEY", "your-api-key")

client = APIClient(BASE_URL, API_KEY)

@pytest.mark.fota
def test_fota_update_request():
    """Verify FOTA update trigger"""
    payload = {
        "vehicleId": "VH12345",
        "softwareVersion": "v2.1.5",
        "updateType": "security_patch"
    }

    response = client.post("fota/trigger", payload)

    assert response.status_code == 202
    assert response.json().get("updateStatus") == "queued"
