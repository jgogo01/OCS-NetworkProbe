from dotenv import load_dotenv, dotenv_values
import sys

load_dotenv()
env = dotenv_values(".env")

# Check if INTERNAL_GATEWAY is missing
if "INTERNAL_GATEWAY" not in env or env["INTERNAL_GATEWAY"] == "":
    print("INTERNAL_GATEWAY is missing in environment variables.")
    sys.exit(1)

# Check if EXTERNAL_GATEWAY is missing
if "EXTERNAL_GATEWAY" not in env or env["EXTERNAL_GATEWAY"] == "":
    print("EXTERNAL_GATEWAY is missing in environment variables.")
    sys.exit(1)

# Check if PING_COUNT is missing
if "PING_COUNT" not in env or not env["PING_COUNT"].isdigit():
    print("PING_COUNT is missing or not a valid number in environment variables.")
    sys.exit(1)

# Check if INTERFACE_LAN is missing
if "INTERFACE_LAN" not in env or env["INTERFACE_LAN"] == "":
    print("INTERFACE_LAN is missing in environment variables.")
    sys.exit(1)

# Check if INTERFACE_WIFI is missing
if "INTERFACE_WIFI" not in env or env["INTERFACE_WIFI"] == "":
    print("INTERFACE_WIFI is missing in environment variables.")
    sys.exit(1)

# Check if WIFI_SSID is missing
if "WIFI_SSID" not in env or env["WIFI_SSID"] == "":
    print("WIFI_SSID is missing in environment variables.")
    sys.exit(1)

# Check if WIFI_BAND is missing
if "WIFI_BAND" not in env or env["WIFI_BAND"] == "":
    print("WIFI_BAND is missing in environment variables.")
    sys.exit(1)

# Check if WIFI_PASSWORD is missing
if "WIFI_PASSWORD" not in env or env["WIFI_PASSWORD"] == "":
    print("WIFI_PASSWORD is missing in environment variables.")
    sys.exit(1)