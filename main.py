import sys
sys.dont_write_bytecode = True

from fastapi import FastAPI
import nest_asyncio
import uvicorn
from routes import general, ping, speedtest
import os

#FastAPI
app = FastAPI()
app.include_router(general.router)
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
    
#Check PROBE_LIST in .env
PROBE_LIST = os.getenv("PROBE_LIST")
if PROBE_LIST == None:
    print("PROBE_LIST is not found in .env")
    sys.exit(1)

#Uvicorn Server
if __name__ == "__main__":
    nest_asyncio.apply()
    uvicorn.run("main:app", port=4000, host="0.0.0.0")