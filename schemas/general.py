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
    def __init__(self, identity, system, uptime, location):
        self.system = System(**system)
        self.uptime = uptime
        self.identity = identity
        self.location = Location(**location)
        
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