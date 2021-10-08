import requests
import json
import time
import random

##################################################
# Get Data From Sensor
##################################################
def get_data():

  # TODO: https://github.com/adafruit/Adafruit_CircuitPython_seesaw/blob/main/examples/seesaw_soil_simpletest.py
  temperature = random.randint(60, 100)
  soil_moisture = random.randint(20, 200)

  # Format for murano
  data_in = {'temperature': temperature, 'soil_moisture': soil_moisture}
  return data_in

##################################################
# Send Data
#################################################
# Get the config from file
configfile = open("config", "r")
device_id = configfile.readline().replace('device_id=', '').strip()
device_endpoint = configfile.readline().replace('device_endpoint=', '').strip()
data_report_rate_seconds = configfile.readline().replace('data_report_rate_seconds=', '').strip()
URL = device_endpoint + '/onep:v1/stack/alias'

# Get the token from file
tokenfile = open("token", "r")
token = tokenfile.read().strip()

print('*****************************************')
print('Device ID: ', device_id)
print('Endpoint: ', device_endpoint)
print('Device Token: ', token)
print('Report Rate: ', data_report_rate_seconds, ' seconds')
print('******************************************')

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/x-www-form-urlencoded; charset=utf-8',
  'X-Exosite-CIK': token
}

config_io = {
  'channels': {
    'temperature': {
      'display_name': 'Temperature',
      'properties': {
        'data_unit': 'DEG_FAHRENHEIT',
        'data_type': 'TEMPERATURE',
      }
    },
    'soil_moisture': {
      'display_name': 'Soil Moisture',
      'properties': {
        'data_type': 'NUMBER',
      }
    }
  }
}

# Send ConfigIO Once
configIO = 'config_io=' + json.dumps(config_io)
requests.post(
  URL,
  headers=headers,
  data=configIO,
)

# Send Data Every XX seconds until the program is terminated
while True:
  newData = get_data()
  print('Sending data: ', json.dumps(newData))
  data = 'data_in=' + json.dumps(newData)
  requests.post(
    URL,
    headers=headers,
    data=data,
  )

  time.sleep(int(data_report_rate_seconds))
