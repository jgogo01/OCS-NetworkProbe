from fastapi import APIRouter
import netifaces

router = APIRouter()

@router.get("/nic")
async def main():
    result = {}
    gateways = netifaces.gateways()
    result["gateways"] = gateways

    interfaces = netifaces.interfaces()
    result["interfaces"] = interfaces

    interface_info = {}
    for interface in interfaces:
        info = netifaces.ifaddresses(interface)
        interface_info[interface] = info
    result["interface_info"] = interface_info
    
    return result
