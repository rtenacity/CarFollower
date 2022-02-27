#!/usr/bin/env python3

# this program tests if an object is too close 

from ev3dev2.motor import MoveSteering, OUTPUT_C, OUTPUT_D, MoveTank, SpeedPercent, follow_for_ms, MoveDifferential
from ev3dev2.sensor.lego import UltrasonicSensor, GyroSensor, InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from sys import stderr
from time import sleep

tank = MoveTank(OUTPUT_D, OUTPUT_C)
us = UltrasonicSensor()
leds = Leds()
spkr = Sound()

leds.all_off() # Needed, to stop the LEDs flashing
while True:
    if us.distance_centimeters > 40: # to detect objects closer than 40cm
        tank.on()
        print(us.distance_centimeters)
    elif us.distance_centimeters < 40:
        tank.off()
        leds.set_color('LEFT',  'RED')
        leds.set_color('RIGHT', 'RED')
        spkr.speak('Too close')
    print(us.distance_centimeters)
    sleep (0.5)

