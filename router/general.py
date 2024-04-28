from fastapi import APIRouter
import psutil
from gpiozero import CPUTemperature
import os
import time

def get_cpu_temp():
  try:
    CPU_TEMP = CPUTemperature().temperature
  except Exception as e:
    CPU_TEMP = 0.0
  return CPU_TEMP

router = APIRouter()

@router.get("/general")
async def main():
  status = 200
  message = "Welcome to OCS API Probe"
  data = {}
  
  try: 
    CPU_TEMP = get_cpu_temp()
    
    data = {
        "system": {
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
        },
        "uptime": time.time() - psutil.boot_time(),
        "location": {
          "latitude": os.getenv("LATITUDE"),
          "longitude": os.getenv("LONGITUDE"),
        }
      }
  except Exception as e:
    status = 500
    message = str(e)
    
  return {
    "status": status,
    "message": message,
    "data": data
  }
  