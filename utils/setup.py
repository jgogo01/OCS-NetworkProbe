import wifi_connection
import os
import sys
from dotenv import load_dotenv

load_dotenv()
INTERFACE_WIFI_FOR_SETUP = os.getenv("INTERFACE_WIFI_FOR_SETUP")
SSID = os.getenv("SSID")
PASSWORD = os.getenv("PASSWORD")
BAND = os.getenv("BAND")

# Get the list of available network interfaces
interfaces = wifi_connection.get_interfaces()
print("Available interfaces:", interfaces)

# Check if INTERFACE_WIFI_FOR_SETUP is valid
if not wifi_connection.get_network_list(INTERFACE_WIFI_FOR_SETUP):
        print("INTERFACE_WIFI_FOR_SETUP isn't correct. Please recheck the interface name.")
        sys.exit(1)

# Set Profile
wifi_connection.set_profile(INTERFACE_WIFI_FOR_SETUP, BAND, SSID, PASSWORD)

# Connect to Wi-Fi
if not wifi_connection.connect(INTERFACE_WIFI_FOR_SETUP, SSID):
    print("Wi-Fi cannot connect. Please recheck the password.")
    sys.exit(1)
    
print("The Wi-Fi connection was successful.")