import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Check if INTERNAL_GATEWAY is missing
INTERNAL_GATEWAY = os.getenv("INTERNAL_GATEWAY")
if not INTERNAL_GATEWAY:
    print("INTERNAL_GATEWAY is missing in environment variables.")
    sys.exit(1)

# Check if EXTERNAL_GATEWAY is missing
EXTERNAL_GATEWAY = os.getenv("EXTERNAL_GATEWAY")
if not EXTERNAL_GATEWAY:
    print("EXTERNAL_GATEWAY is missing in environment variables.")
    sys.exit(1)

# Check if PING_COUNT is missing
PING_COUNT = os.getenv("PING_COUNT")
if not PING_COUNT or not PING_COUNT.isdigit():
    print("PING_COUNT is missing or not a valid number in environment variables.")
    sys.exit(1)

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

# Check if SSID is missing
SSID = os.getenv("SSID")
if not SSID:
    print("SSID is missing in environment variables.")
    sys.exit(1)

# Check if ENCRYPTION is missing
PASSWORD = os.getenv("PASSWORD")
if not PASSWORD:
    print("PASSWORD is missing in environment variables.")
    sys.exit(1)
    
# Check if LATITUDE is missing
LATTITUDE = os.getenv("LATITUDE")
if not LATTITUDE:
    print("LATITUDE is missing in environment variables.")
    sys.exit(1)
    
# Check if LONGITUDE is missing
LONGITUDE = os.getenv("LONGITUDE")
if not LONGITUDE:
    print("LONGITUDE is missing in environment variables.")
    sys.exit(1)
    
print("All required environment variables are present.")