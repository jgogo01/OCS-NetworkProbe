import sys

# Disable Bytecode
sys.dont_write_bytecode = True

from utils.validation import *
from utils.setup import *
from fastapi import FastAPI
from routers import ping, speedtest, nic, general
from dotenv import load_dotenv
from gunicorn.app.base import BaseApplication
import uvicorn
import multiprocessing
    
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
def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class StandaloneApplication(BaseApplication):
    def __init__(self, application: Callable, options: Dict[str, Any] = None):
        self.options = options or {}
        self.application = application
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == "__main__":
    options = {
        "bind": "%s:%s" % ("0.0.0.0", "4000"),
        "workers": number_of_workers(),
        "worker_class": "uvicorn.workers.UvicornWorker",
    }
    StandaloneApplication(app, options).run()
