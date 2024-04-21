class SpeedtestResult:
  def __init__(self, status, message, data):
    self.status = status
    self.message = message
    self.data = Data(data)

class Data:
  def __init__(self, data):
    self.timestamp = data["timeStamp"]
    self.lan = LAN(data["lan"])
    self.wifi = WIFI(data["wifi"])

class LAN:
  def __init__(self, lan_data):
    self.src = lan_data["src"]
    self.speedtest = SpeedTest(lan_data["speedtest"])

class WIFI:
  def __init__(self, wifi_data):
    self.src = wifi_data["src"]
    self.speedtest = SpeedTest(wifi_data["speedtest"])

class SpeedTest:
  def __init__(self, speedtest_data):
    self.server = Server(speedtest_data["server"])
    self.download = speedtest_data["download"]
    self.upload = speedtest_data["upload"]

class Server:
  def __init__(self, server_data):
    self.url = server_data["url"]
    self.lat = server_data["lat"]
    self.lon = server_data["lon"]
    self.name = server_data["name"]
    self.country = server_data["country"]
    self.cc = server_data["cc"]
    self.sponsor = server_data["sponsor"]
    self.id = server_data["id"]
    self.host = server_data["host"]
    self.distance = server_data["d"]  # Assuming "d" stands for distance
    self.latency = server_data["latency"]