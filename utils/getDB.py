from py_directus import Directus
from dotenv import load_dotenv
from interfaces import Setting
from pydantic import ConfigDict
import os

load_dotenv()
TOKEN_DIRECTUS = os.getenv("TOKEN_DIRECTUS")
HOST_DIRECTUS = os.getenv("HOST_DIRECTUS")

async def getDB():
    try:
        directus = await Directus(HOST_DIRECTUS, token=TOKEN_DIRECTUS)
        model_config = ConfigDict(collection="setting")
        directus.collection(Setting)

    except Exception as e:
        print(f"Error initializing Directus: {str(e)}")
        return None   
