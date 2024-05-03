import sys
#Disable Bytecode
sys.dont_write_bytecode = True

from utils.validation import *
from utils.setup import *
from fastapi import FastAPI
from router import ping, speedtest, nic, general, network
import nest_asyncio
import uvicorn
from dotenv import load_dotenv

load_dotenv()

#FastAPI
app = FastAPI()
app.include_router(ping.router)
app.include_router(speedtest.router)
app.include_router(nic.router)
app.include_router(general.router)
app.include_router(network.router)

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
if __name__ == "__main__":
    nest_asyncio.apply()
    uvicorn.run("main:app", port=4000, host="0.0.0.0", workers=5)