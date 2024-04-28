import requests
from schemas.speedtest import SpeedtestResult
from fastapi import APIRouter
from utils.prometheus import *

router = APIRouter()

@router.get("/metrics/speedtest/")
async def metrics(target: str):
    try:
        speedtest = requests.get(f"http://{target}/speedtest").json()
        result = SpeedtestResult(speedtest["status"], speedtest["message"], speedtest["data"])
        
        #Set Prometheus metrics
        LAN_ST_DOWNLOAD.set(result.data.lan.speedtest.download)
        LAN_ST_UPLOAD.set(result.data.lan.speedtest.upload)
        WLAN_ST_DOWNLOAD.set(result.data.wlan.speedtest.download)
        WLAN_ST_UPLOAD.set(result.data.wlan.speedtest.upload)
        
        return {
            "status": 200,
            "message": "Updated Prometheus metrics",
            "data": {}
        }
    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": {}
        }