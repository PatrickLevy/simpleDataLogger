# Simple Data Logger
1. Enable "Interface Options" -> "I2C" by typing `sudo raspi-config` to enter configuration menu
2. Clone this repo
3. Fill out the `config` file (don't include a slash at the end of your endpoint)
4. Provision your device: `python3 provision.py`
5. Send data to your device: `python3 dataLogger.py`
