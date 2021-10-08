# Simple Data Logger for Raspberry Pi
1. Enable "Interface Options" -> "I2C" by typing `sudo raspi-config` to enter configuration menu
2. Install libraries: `pip3 install adafruit-circuitpython-seesaw`
3. See here for wiring to raspberry pi: [Adafruit Soil Sensor Wiring for Python](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test)
4. Clone this repo `git clone https://github.com/PatrickLevy/simpleDataLogger.git`
5. Fill out the `config` file (don't include a slash at the end of your endpoint)
6. Provision your device: `python3 provision.py`
7. Send data to your device: `python3 dataLogger.py`
