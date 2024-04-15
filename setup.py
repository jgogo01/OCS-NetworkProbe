import wifi_connection
from dotenv import load_dotenv, dotenv_values
load_dotenv()
env = dotenv_values(".env")

profile = wifi_connection.set_profile(env["INTERFACE_WIFI"], env["WIFI_BAND"], env["WIFI_SSID"], env["WIFI_PASSWORD"])
try:
    success = wifi_connection.connect(env["INTERFACE_WIFI"], env["WIFI_SSID"])
    connected_ssid = wifi_connection.get_ssid(env["INTERFACE_WIFI"])
    connection_info = wifi_connection.get_connection_info(env["INTERFACE_WIFI"])
    print("Profile set successfully:", profile)
    print("Connection successful:", success)
    print("Connected SSID:", connected_ssid)
    print("Connection information for", env["INTERFACE_WIFI"], connection_info)
except:
    print("Error")