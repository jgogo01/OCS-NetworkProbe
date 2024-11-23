import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Check if INTERFACE_LAN is missing
INTERFACE_LAN = os.getenv("INTERFACE_LAN")
if not INTERFACE_LAN:
    print("INTERFACE_LAN is missing in environment variables.")
    sys.exit(1)

# Check if INTERFACE_WLAN is missing
INTERFACE_WLAN = os.getenv("INTERFACE_WLAN")
if not INTERFACE_WLAN:
    print("INTERFACE_WLAN is missing in environment variables.")
    sys.exit(1)
    

    
print("All required environment variables are present.")