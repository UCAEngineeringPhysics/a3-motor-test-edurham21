"""
Ramp up motors' speed forward in 4 seconds. 
Slow down motors' speed forward in 4 seconds. 
Ramp up motors' speed backward in 4 seconds. 
Slow down motors' speed backward in 4 seconds. 
Stop motors.
"""
from machine import Pin, PWM
from time import sleep

# SETUP
#configure pins for left motor
INA_LEFT = Pin(7, Pin.OUT)
INB_LEFT = Pin(8, Pin.OUT)
INA_LEFT.off()
INB_LEFT.off()
PWM_LEFT = PWM(Pin(6))
PWM_LEFT.freq(1000)

#configure pins for right motor
INA_RIGHT = Pin(11, Pin.OUT)
INB_RIGHT = Pin(12, Pin.OUT)
PWM_RIGHT = PWM(Pin(10))
PWM_RIGHT.freq(1000)
INA_RIGHT.off()
INB_RIGHT.off()

#set max duty
max_duty = 65025

#set ramp time
ramp_time = 4

#set step size
step_size = 500
steps = max_duty // step_size #integer division to find steps

#calculate time to sleep for each step
ramp_step = ramp_time / steps

# LOOP
