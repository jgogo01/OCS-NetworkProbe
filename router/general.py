from fastapi import APIRouter
import psutil
from gpiozero import CPUTemperature
import os
import time

router = APIRouter()

def get_system_info():
  try:
    CPU_TEMP = CPUTemperature().temperature
  except Exception as e:
    CPU_TEMP = None
  return {
      "cpu": {
          "core": psutil.cpu_count(logical=False),
          "thread": psutil.cpu_count(logical=True),
          "usage": psutil.cpu_percent(),
          "temperature": CPU_TEMP,
      },
      "ram": {
          "usage": psutil.virtual_memory().used,
          "available": psutil.virtual_memory().available,
          "total": psutil.virtual_memory().total,
      },
  }

@router.get("/general")
async def main():
  return {
      "status": 200,
      "message": "Welcome to OCS API Probe",
      "data": {
        "system": get_system_info(),
        "uptime": time.time() - psutil.boot_time(),
        "location": {
          "latitude": os.getenv("LATITUDE"),
          "longitude": os.getenv("LONGITUDE"),
        }
      }
  }
