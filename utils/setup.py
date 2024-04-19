import os
from dotenv import load_dotenv

load_dotenv()

SSID = os.getenv("SSID")
PASSWORD = os.getenv("PASSWORD")
INTERFACE_WIFI = os.getenv("INTERFACE_WIFI")

class WifiFinder:
    def __init__(self, *args, **kwargs):
        self.ssid = kwargs['ssid']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

    def run(self):
        command = """iwlist wlp2s0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        result = os.popen(command.format(self.ssid))
        result = list(result)

        if "Device or resource busy" in result:
                return None
        else:
            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
            print("Successfully get ssids {}".format(str(ssid_list)))

        for name in ssid_list:
            try:
                result = self.connection(name)
            except Exception as exp:
                print("Couldn't connect to name : {}. {}".format(name, exp))
            else:
                if result:
                    print("Successfully connected to {}".format(name))

    def connection(self, name):
        try:
            os.system("nmcli d wifi connect {} password {} iface {}".format(name,
       self.password,
       self.interface_name))
        except:
            raise
        else:
            return True



WF = WifiFinder(ssid=SSID, password=PASSWORD, interface=INTERFACE_WIFI)
WF.run()