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

# Check if INTERFACE_WIFI is missing
INTERFACE_WIFI = os.getenv("INTERFACE_WIFI")
if not INTERFACE_WIFI:
    print("INTERFACE_WIFI is missing in environment variables.")
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

# Check if AUTHENTICATION is missing
AUTHENTICATION = os.getenv("AUTHENTICATION")
if not AUTHENTICATION:
    print("AUTHENTICATION is missing in environment variables.")
    sys.exit(1)

# Check if ENCRYPTION is missing
ENCRYPTION = os.getenv("ENCRYPTION")
if not ENCRYPTION:
    print("ENCRYPTION is missing in environment variables.")
    sys.exit(1)

# Check if USEONEX is missing
USEONEX = os.getenv("USEONEX")
if not USEONEX or not USEONEX.isdigit():
    print("USEONEX is missing or not a valid number in environment variables.")
    sys.exit(1)
else:
    if int(USEONEX):
        # Check if EAP_METHOD is missing
        EAP_METHOD = os.getenv("EAP_METHOD")
        if not EAP_METHOD:
            print("EAP_METHOD is missing in environment variables.")
            sys.exit(1)

        # Check if PHASE2_AUTH is missing
        PHASE2_AUTH = os.getenv("PHASE2_AUTH")
        if not PHASE2_AUTH:
            print("PHASE2_AUTH is missing in environment variables.")
            sys.exit(1)

        # Check if DOT1X_USERNAME is missing
        DOT1X_USERNAME = os.getenv("DOT1X_USERNAME")
        if not DOT1X_USERNAME:
            print("DOT1X_USERNAME is missing in environment variables.")
            sys.exit(1)

        # Check if DOT1X_PASSWORD is missing
        DOT1X_PASSWORD = os.getenv("DOT1X_PASSWORD")
        if not DOT1X_PASSWORD:
            print("DOT1X_PASSWORD is missing in environment variables.")
            sys.exit(1)
    
print("All required environment variables are present.")