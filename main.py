import sys

# Disable Bytecode
sys.dont_write_bytecode = True

from utils.validation import *
from utils.setup import *
from fastapi import FastAPI
from routers import ping, speedtest, nic, general
from dotenv import load_dotenv
from gunicorn.app.base import BaseApplication
from multiprocessing import cpu_count
    
load_dotenv()

# FastAPI
app = FastAPI()
app.include_router(ping.router)
app.include_router(speedtest.router)
app.include_router(nic.router)
app.include_router(general.router)

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

# Use Gunicorn with Uvicorn workers
if __name__ == "__main__":
    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key.lower(), value)

        def load(self):
            return self.application

    uvicorn_options = {
        'host': '0.0.0.0',
        'port': 8000,
        'log_level': 'info',
        'workers': cpu_count() * 2 + 1  # Adjust workers as per your requirement
    }

    standalone_app = StandaloneApplication(app, uvicorn_options)
    standalone_app.run()