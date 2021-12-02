
'''
This script will run the backend of our automated aquaponics system. 

It's job is to manage reading sensor settings, and uploading them to our databse. It will also control things such as the automatic feeder.
Created by Dylan Lawrence on 11/30/2021
'''

#import dependencies
from datetime import timedelta, datetime

from helper_functions import record_temperature_data, read_temp
from stepper_functions import rotate_motor


#Record starting time and assign it to the variables that will be used to check if it is time to take a reading
temperature_time = datetime.now()
feeder_time = datetime.now()

#datetime constants for interval between reads
TEMPERATURE_INTERVAL = timedelta(minutes = 1)
FEEDER_INTERVAL = timedelta(seconds = 30)
#start never ending while loop
while True:
    if datetime.now() >= temperature_time + TEMPERATURE_INTERVAL:
        print("Recording Temperature")
        record_temperature_data()
        temperature_time = datetime.now()

    #Feed fish
    if datetime.now() >= feeder_time + FEEDER_INTERVAL:
        print("Feeding Fish")
        rotate_motor(1)
        feeder_time = datetime.now()