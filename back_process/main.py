"""
This script will run the backend of our automated aquaponics system.

It's job is to manage reading sensor settings, and uploading them to our database.
It will also control things such as the automatic feeder.
Created by Dylan Lawrence on 11/30/2021
"""

# import dependencies
import RPi.GPIO as GPIO
from datetime import date, timedelta, datetime
from time import time
from helper_functions import record_temperature_data, read_temp, record_action
from stepper_functions import rotate_motor
from ISStreamer.Streamer import Streamer
import time

# Record starting time and assign it to the variables that will be used to check if it is time to take a reading
temperature_time = datetime.now()
feeder_time = datetime.now()
pump_time = datetime.now()
pump_on = False
PUMP_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.output(PUMP_PIN, GPIO.HIGH)

# setup up ISS streamer
streamer = Streamer(
    bucket_name="aquaponics",
    bucket_key="PUP53NDXKYPQ",
    access_key="ist_7iQFeMt52V3ZoqtP7c1cc368avpJUHfw"
)

# datetime constants for interval between reads
TEMPERATURE_INTERVAL = timedelta(seconds=10)
FEEDER_INTERVAL = timedelta(minutes=1)
PUMP_INTERVAL = timedelta(minutes=2)
PUMP_TIME_ON = timedelta(minutes=1)

# start never ending while loop
while True:
    if datetime.now() >= temperature_time + TEMPERATURE_INTERVAL:
        print("Recording Temperature")
        temperature = round(record_temperature_data(), 2)
        temperature_time = datetime.now()
        streamer.log("temperature", temperature)
        streamer.log("last_temp_time", str(datetime.now()))
        streamer.flush()
        record_action("temperature-read")

    # Feed fish
    if datetime.now() >= feeder_time + FEEDER_INTERVAL:
        print("Feeding Fish")
        rotate_motor(1)
        feeder_time = datetime.now()
        record_action("fish-fed")
        streamer.log("last_fed_time", str(datetime.now()))
        streamer.flush()

    if datetime.now() >= pump_time + PUMP_INTERVAL and pump_on == False:
        print("Pump On")
        GPIO.output(PUMP_PIN, GPIO.LOW)
        pump_time = datetime.now()
        pump_on = True
        record_action("pump-on")

    if datetime.now() >= pump_time + PUMP_TIME_ON and pump_on == True:
        print("Pump Off")
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        pump_time = datetime.now()
        pump_on = False
        record_action("pump-off")
