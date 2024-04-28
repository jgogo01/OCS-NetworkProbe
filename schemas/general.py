class GeneralResult:
    def __init__(self, status: int, message: str, data: dict):
        self.status = status
        self.message = message
        self.data = Data(**data)

class Location:
    def __init__(self, latitude: str, longitude: str):
        self.latitude = latitude
        self.longitude = longitude
        
class Data:
    def __init__(self, system: dict, uptime: float, location: Location):
        self.system = System(**system)
        self.uptime = uptime
        self.location = location
        
class System:
    def __init__(self, cpu: dict, ram: dict):
        self.cpu = CPU(**cpu)
        self.ram = RAM(**ram)

class CPU:
    def __init__(self, core: int, thread: int, usage: float, temperature: float):
        self.core = core
        self.thread = thread
        self.usage = usage
        self.temperature = temperature
        
class RAM:
    def __init__(self, usage: int, available: int, total: int):
        self.usage = usage
        self.available = available
        self.total = total