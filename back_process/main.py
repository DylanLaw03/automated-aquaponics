'''
This script will run the backend of our automated aquaponics system. 
It's job is to manage reading sensor settings, and uploading them to our databse. It will also control things such as the automatic feeder.

Created by Dylan Lawrence on 11/30/2021
'''

#import dependencies
from datetime import datetime
from helper_functions import read_temp

#Record starting time and assign it to the variables that will be used to check if it is time to take a reading
temperature_time = datetime.now()

#start never ending while loop
print(read_temp())
