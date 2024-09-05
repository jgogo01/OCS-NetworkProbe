import requests
from schemas.speedtest import SpeedtestResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.speedtest import * 
from requests.adapters import HTTPAdapter

router = APIRouter()

session = requests.Session()
adapter = HTTPAdapter(max_retries=10)
session.mount('http://', adapter)
session.mount('https://', adapter)

@router.get("/metrics/speedtest/")
async def metrics(target: str):
    try:
        speedtest = session.get(f"http://{target}/speedtest").json()
        result = SpeedtestResult(speedtest["status"], speedtest["message"], speedtest["data"])
        
        #Set Prometheus metrics
        LAN_ST_DOWNLOAD.set(result.data.lan.speedtest.download)
        LAN_ST_UPLOAD.set(result.data.lan.speedtest.upload)
        WLAN_ST_DOWNLOAD.set(result.data.wlan.speedtest.download)
        WLAN_ST_UPLOAD.set(result.data.wlan.speedtest.upload)
        
        return Response(
        media_type="text/plain",
        content=generate_latest(registry=speedtest_registry)
        )
    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": {}
        }