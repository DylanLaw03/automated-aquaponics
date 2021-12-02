#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
 
in1 = 17
in2 = 18
in3 = 27
in4 = 22
 
#time in between steps
sleep_time = 0.002
 
 
direction = "counterclockwise" 
 
#Set direction to "clockwise" or "counterclockwise"

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

def rotate_motor(num_rotations):
    step_count = 4096 * num_rotations #4096 is the number of steps for a full rotation
    #set up pins
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    
    
    motor_pins = [in1,in2,in3,in4]
    step_counter = 0 ;

    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output(motor_pins[pin], step_sequence[step_counter][pin])
        if direction == 'clockwise':
            step_counter = (step_counter - 1) % 8
        elif direction == 'counterclockwise':
            step_counter = (step_counter + 1) % 8
        time.sleep(sleep_time)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
