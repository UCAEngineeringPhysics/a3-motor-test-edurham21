"""
Spin motors for 1 minute
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

# LOOP
INB_LEFT.on()
PWM_LEFT.duty_u16(int(65025 / 2)) #1/2 max speed
INB_RIGHT.on()
PWM_RIGHT.duty_u16(int(65025 / 2))
sleep(60) #Sleep for 1 minute

INB_LEFT.off()
INB_RIGHT.off()
PWM_LEFT.duty_u16(0)
PWM_RIGHT.duty_u16(0)