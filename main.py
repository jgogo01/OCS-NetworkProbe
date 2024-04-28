import sys
sys.dont_write_bytecode = True

from fastapi import FastAPI
from routes import metrics
import nest_asyncio
import uvicorn
from utils.prometheus import *
from routes import dns, metrics, general, ip, ping, speedtest


#FastAPI
app = FastAPI()
app.include_router(metrics.router)
app.include_router(dns.router)
app.include_router(general.router)
app.include_router(ip.router)
app.include_router(ping.router)
app.include_router(speedtest.router)

@app.get("/")
async def main():
    status = 200
    message = "Welcome to OCS Explorer Probe"
    data = {}

    return {
        "status": status,
        "message": message,
        "data": data
    }

#Uvicorn Server
nest_asyncio.apply()
uvicorn.run(app, port=4000, host="0.0.0.0")