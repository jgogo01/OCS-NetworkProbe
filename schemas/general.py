class GeneralResult:
    def __init__(self, status, message, data):
        self.status = status
        self.message = message
        self.data = Data(**data)

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        
class Data:
    def __init__(self, identity, system, uptime, location, network):
        self.identity = identity
        self.system = System(**system)
        self.uptime = uptime
        self.location = Location(**location)
        self.network = Network(**network)
        
class System:
    def __init__(self, cpu, ram):
        self.cpu = CPU(**cpu)
        self.ram = RAM(**ram)

class CPU:
    def __init__(self, core, thread, usage, temperature):
        self.core = core
        self.thread = thread
        self.usage = usage
        self.temperature = temperature
        
class RAM:
    def __init__(self, usage, available, total):
        self.usage = usage
        self.available = available
        self.total = total
        
class Network:
    def __init__(self, lan, wlan):
        self.lan = LAN(**lan)
        self.wlan = WLAN(**wlan)

class LAN:
    def __init__(self, ipv4_and_ipv6, ipv4, ipv6, dns):
        self.ipv4_and_ipv6 = ipv4_and_ipv6
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.dns = DNS(**dns)
        
class WLAN:
    def __init__(self, ipv4_and_ipv6, ipv4, ipv6, dns):
        self.ipv4_and_ipv6 = ipv4_and_ipv6
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.dns = DNS(**dns)

class DNS:
    def __init__(self, status, hostname, ip_address, response_time):
        self.status = status
        self.hostname = hostname
        self.ip_address = ip_address
        self.response_time = response_time