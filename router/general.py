from fastapi import APIRouter
import psutil
import os
import time

def get_cpu_temp():
  try:
    cpu_temperatures = psutil.sensors_temperatures()
    coretemp_temperatures = cpu_temperatures.get('coretemp', [])
    if coretemp_temperatures:
        core_0_temp = coretemp_temperatures[0]
        cpu_temp = core_0_temp.current
        return cpu_temp
    else:
      return 0
  except Exception as e:
    return 0

router = APIRouter()

@router.get("/general")
async def main():
  status = 200
  message = "Welcome to OCS API Probe"
  data = {}
  
  try: 
    CPU_TEMP = get_cpu_temp()
    
    data = {
        "identity": os.getenv("IDENTITY"),
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
  