import requests
from schemas.general import GeneralResult
from fastapi import APIRouter, Response
from prometheus_client import generate_latest
from utils.prometheus import *

router = APIRouter()

@router.get("/metrics/general/")
async def metrics(target: str):
    try:
        general = requests.get("http://{target}:4000/general").json()
        result = GeneralResult(general["status"], general["message"], general["data"])
        
        #Set Prometheus metrics
        CPU_CORE.set(result.data.system.cpu.core)
        CPU_THREAD.set(result.data.system.cpu.thread)
        CPU_USAGE.set(result.data.system.cpu.usage)
        CPU_TEMPERATURE.set(result.data.system.cpu.temperature)
        RAM_USAGE.set(result.data.system.ram.usage)
        RAM_AVAILABLE.set(result.data.system.ram.available)
        RAM_TOTAL.set(result.data.system.ram.total)
        UPTIME.set(result.data.uptime)
        LATITUDE.info(result.data.location.latitude)
        LONGITUDE.info(result.data.location.longitude)
        
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