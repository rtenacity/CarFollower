#!/usr/bin/python
# coding: utf-8

# this program lets your ev3 follow a toy car accurately

from ev3dev2.motor import *
from ev3dev2.sensor.lego import UltrasonicSensor, GyroSensor, InfraredSensor, TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from sys import stderr
from time import sleep

left_motor = LargeMotor(OUTPUT_C) 
right_motor = LargeMotor(OUTPUT_D)
us = UltrasonicSensor()
ts = TouchSensor()

correction = 0

kp = 1 
power = 60
target = 10


left_motor.run_direct()
right_motor.run_direct()

print("Target, Distance, Error, Correction")
while True:
    error = target - us.distance_centimeters #

    if ts.value():
        break
    if error < 0: #if the error is less than 0 (too far from the car), the car speeds up. 
        correction = (abs(float(error)/5))*kp
        if (correction+power) >= 100 or (correction+power) <= -100: #to make sure the code doesn't error out
            correction = -(power)

    if error > 0: #if the error is more than 0 (too close from the car), the car stops. 
        correction = -(power)
    if error == 0: #if the error is equal than 0 (perfect distance from car), the car stops. 
        correction = -(power)
    if us.distance_centimeters == 255.0: #the ultrasonic sensor has an error where it reads 255, so this line makes sure it doesn't glitch out and mess up the algorithm.
        correction = -(power)

    print(str(target)+", "+str(us.distance_centimeters)+", "+str(error)+", "+str(correction)) #for debugging, comment out if not needed
    left_motor.duty_cycle_sp= int(-(power + correction)) #sets the wheel speed (negative because my robot's wheels are backward)
    right_motor.duty_cycle_sp= int(-(power + correction)) #sets the wheel speed (negative because my robot's wheels are backward)
    sleep(0.1)
left_motor.stop()
right_motor.stop()