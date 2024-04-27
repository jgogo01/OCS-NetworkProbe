from fastapi import APIRouter
import dns

router = APIRouter()

@router.get("/dns")
async def main():        
    return {
        "status": 200,
        "message": "Welcome to OCS API Probe",
        "data": {}
    }