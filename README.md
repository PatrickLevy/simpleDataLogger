# Simple Data Logger for Raspberry Pi
1. Enable "Interface Options" -> "I2C" by typing `sudo raspi-config` to enter configuration menu
2. See here for wiring to raspberry pi: [Adafruit Soil Sensor With CircuitPython](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test)
3. Clone this repo `git clone https://github.com/PatrickLevy/simpleDataLogger.git`
4. Fill out the `config` file (don't include a slash at the end of your endpoint)
5. Provision your device: `python3 provision.py`
6. Send data to your device: `python3 dataLogger.py`
