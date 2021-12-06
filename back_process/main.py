
'''
This script will run the backend of our automated aquaponics system. 

It's job is to manage reading sensor settings, and uploading them to our databse. It will also control things such as the automatic feeder.
Created by Dylan Lawrence on 11/30/2021
'''

#import dependencies
from datetime import date, timedelta, datetime

from helper_functions import record_temperature_data, read_temp, record_action
from stepper_functions import rotate_motor
from ISStreamer.Streamer import Streamer

#Record starting time and assign it to the variables that will be used to check if it is time to take a reading
temperature_time = datetime.now()
feeder_time = datetime.now()

#setp up ISS streamer
streamer = Streamer(
    bucket_name="aquaponics",
    bucket_key="PUP53NDXKYPQ",
    access_key="ist_7iQFeMt52V3ZoqtP7c1cc368avpJUHfw"
)



#datetime constants for interval between reads
TEMPERATURE_INTERVAL = timedelta(seconds = 10)
FEEDER_INTERVAL = timedelta(seconds = 30)
#start never ending while loop
while True:
    if datetime.now() >= temperature_time + TEMPERATURE_INTERVAL:
        print("Recording Temperature")
        temperature = round(record_temperature_data(), 2)
        temperature_time = datetime.now()
        streamer.log("temperature", temperature)
        streamer.log("last_temp_time", str(datetime.now()))
        streamer.flush()
        record_action("temperature-read")

    if temperature_time + TEMPERATURE_INTERVAL >= datetime.now():
        streamer.log("temp_status", "Error")

    #Feed fish
    if datetime.now() >= feeder_time + FEEDER_INTERVAL:
        print("Feeding Fish")
        rotate_motor(1)
        feeder_time = datetime.now()
        record_action("fish-fed")
        streamer.log("last_fed_time", str(datetime.now()))
        streamer.flush()