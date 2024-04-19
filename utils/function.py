import os
from dotenv import load_dotenv
from utils.function import *

load_dotenv()

ENCRYPTION = os.getenv("ENCRYPTION")
AUTHENTICATION = os.getenv("AUTHENTICATION")

def create_new_connection_windows(name, ssid, password):
    config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>""" + name + """</name>
        <SSIDConfig>
            <SSID>
                <name>""" + ssid + """</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>""" + AUTHENTICATION + """</authentication>
                    <encryption>""" + ENCRYPTION + """</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>""" + password + """</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
    with open(name + ".xml", 'w') as file:
        file.write(config)
    command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
    os.system(command)