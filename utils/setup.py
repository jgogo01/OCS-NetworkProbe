import platform
import subprocess
import os
from dotenv import load_dotenv
from utils.function import *

load_dotenv()

SSID = os.getenv("SSID")
ENCRYPTION = os.getenv("ENCRYPTION")
AUTHENTICATION = os.getenv("AUTHENTICATION")
PASSWORD = os.getenv("PASSWORD")

#802.1x
USEONEX = os.getenv("USEONEX")
EAP_METHOD = os.getenv("EAP_METHOD")
PHASE2_AUTH = os.getenv("PHASE2_AUTH")
DOT1X_USERNAME = os.getenv("DOT1X_USERNAME")
DOT1X_PASSWORD = os.getenv("DOT1X_PASSWORD")

def connect_windows():
    command = "netsh wlan connect name=\"" + SSID + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
    os.system(command)

def connect_linux():
    if USEONEX:
        add_connection_command = ["nmcli", "device", "wifi", "connect", SSID, "password", PASSWORD, "802-1x.eap",
                                  EAP_METHOD, "802-1x.phase2-auth", PHASE2_AUTH, "802-1x.identity", DOT1X_USERNAME, 
                                  "802-1x.password", DOT1X_PASSWORD]
    else:
        if ENCRYPTION.lower() == "none":
            add_connection_command = ["nmcli", "device", "wifi", "connect", SSID]
        else:
            add_connection_command = ["nmcli", "device", "wifi", "connect", SSID, "password", PASSWORD]
    try:
        subprocess.run(add_connection_command, check=True)
        print("Connected to", SSID)
    except subprocess.CalledProcessError:
        print("Failed to connect to", SSID)

if platform.system() == "Windows":
    create_new_connection_windows()
    connect_windows()
    os.remove(SSID + ".xml")
elif platform.system() == "Linux":
    connect_linux()
else:
    print("Unsupported operating system")
