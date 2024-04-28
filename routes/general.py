import requests
from schemas.general import GeneralResult
from fastapi import APIRouter
from utils.prometheus import *

router = APIRouter()

@router.get("/metrics/general")
async def metrics(target: str):
    try:
        general = requests.get(f"http://{target}/general").json()
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
        LOCATION.info({
            "latitude": result.data.location.latitude,
            "longitude": result.data.location.longitude
        })
        
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