from utils.validation import *
from fastapi import FastAPI
from router import ping, speedtest, nic
import nest_asyncio
import uvicorn

#FastAPI
app = FastAPI()
app.include_router(ping.router)
app.include_router(speedtest.router)
app.include_router(nic.router)

@app.get("/")
async def main():
    status = 200
    message = "Welcome to OCS API Probe"
    data = {}

    return {
        "status": status,
        "message": message,
        "data": data
    }

#Uvicorn Server
nest_asyncio.apply()
uvicorn.run(app, port=4000, host="0.0.0.0")