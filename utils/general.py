import psutil

def get_cpu_temp():
  try:
    cpu_temperatures = psutil.sensors_temperatures()
    coretemp_temperatures = cpu_temperatures.get('coretemp', [])
    if coretemp_temperatures:
        core_0_temp = coretemp_temperatures[0]
        cpu_temp = core_0_temp.current
        return cpu_temp
    else:
      return 0
  except Exception as e:
    return 0