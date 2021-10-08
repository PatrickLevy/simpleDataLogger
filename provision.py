import requests
import json

# Get the config from file
configfile = open("config", "r")
device_id = configfile.readline().replace('device_id=', '').strip()
device_endpoint = configfile.readline().replace('device_endpoint=', '').strip()
URL = device_endpoint + '/provision/activate'

# Provision Device
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}
data = 'sn=' + device_id
response = requests.post(
  URL,
  headers=headers,
  data=data,
)

if response.status_code == 200:
  token = response.text
  f = open("token", "w")
  f.write(token)
  print('Device provisioned: ', device_id)
else:
  print(response.status_code)
  print('Could not provision device')