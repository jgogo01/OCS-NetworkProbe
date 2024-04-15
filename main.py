from fastapi import FastAPI
from router import ping, speedtest

app = FastAPI()
app.include_router(ping.router)
app.include_router(speedtest.router)

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