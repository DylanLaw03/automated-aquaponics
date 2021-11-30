from datetime import datetime
import os
import glob
import time
import json
import mysql.connector
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f


def record_temperature_data():
    #load credentials and connect to the database
    credentials = json.load(open("credentials.json", "r"))

    database = mysql.connector.connect(
        host=credentials["host"],
        user=credentials["user"],
        passwd=credentials["password"],
        database=credentials["database"]
    )

    #insert command
    insert_command = "INSERT INTO `temperature_data` (`timestamp`, `temperature`) VALUES (%s, %s);"

    #create set of data
    time = datetime.now()
    data = (time, read_temp())

    #cursor object to execute database commands
    cursor = database.cursor()
    
    #send data to database
    cursor.execute(insert_command,data)
    database.commit()

    #close connection
    cursor.close()
    database.close()