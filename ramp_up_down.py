"""
Ramp up motors' speed forward in 4 seconds. 
Slow down motors' speed forward in 4 seconds. 
Ramp up motors' speed backward in 4 seconds. 
Slow down motors' speed backward in 4 seconds. 
Stop motors.
"""

#ChatGPT added a timer for the ramp up and ramp down time
#I used my microcontrollers program as a reference for this. 

from machine import Pin, PWM
from time import sleep, time

# SETUP
# Configure pins for left motor
INA_LEFT = Pin(7, Pin.OUT)
INB_LEFT = Pin(8, Pin.OUT)
PWM_LEFT = PWM(Pin(6))
PWM_LEFT.freq(1000)

# Configure pins for right motor
INA_RIGHT = Pin(11, Pin.OUT)
INB_RIGHT = Pin(12, Pin.OUT)
PWM_RIGHT = PWM(Pin(10))
PWM_RIGHT.freq(1000)

# LOOP
try:
    while True:
        ramp_time = 4  # 4 seconds for ramping up and down
        
        # Ramp up both motors for forward direction
        start_time = time()
        while time() - start_time < ramp_time:
            elapsed_time = time() - start_time
            speed = int(65025 * elapsed_time / ramp_time)

            # Set forward direction for both motors
            INB_LEFT.on()
            INA_LEFT.off()
            INB_RIGHT.on()
            INA_RIGHT.off()

            # Apply the PWM duty cycle for ramp up
            PWM_LEFT.duty_u16(speed)
            PWM_RIGHT.duty_u16(speed)
            
            # Print elapsed time
            print(f"Elapsed time for ramp up: {elapsed_time:.2f} seconds")
            sleep(0.1)

        # Slow down both motors for forward direction
        start_time = time()
        while time() - start_time < ramp_time:
            elapsed_time = time() - start_time
            speed = int(65025 * (1 - elapsed_time / ramp_time))

            # Set forward direction for both motors
            INB_LEFT.on()
            INA_LEFT.off()
            INB_RIGHT.on()
            INA_RIGHT.off()

            # Apply the PWM duty cycle for slowing down
            PWM_LEFT.duty_u16(speed)
            PWM_RIGHT.duty_u16(speed)

            # Print elapsed time
            print(f"Elapsed time for slow down: {elapsed_time:.2f} seconds")
            sleep(0.1)

        # Ramp up both motors for backwards direction
        start_time = time()
        while time() - start_time < ramp_time:
            elapsed_time = time() - start_time
            speed = int(65025 * elapsed_time / ramp_time)

            # Set backward direction for both motors
            INA_LEFT.on()
            INB_LEFT.off()
            INA_RIGHT.on()
            INB_RIGHT.off()

            # Apply the PWM duty cycle for ramp up
            PWM_LEFT.duty_u16(speed)
            PWM_RIGHT.duty_u16(speed)

            # Print elapsed time
            print(f"Elapsed time for ramp up (backward): {elapsed_time:.2f} seconds")
            sleep(0.1)

        # Slow down both motors for backwards direction
        start_time = time()
        while time() - start_time < ramp_time:
            elapsed_time = time() - start_time
            speed = int(65025 * (1 - elapsed_time / ramp_time))

            # Set backward direction for both motors
            INA_LEFT.on()
            INB_LEFT.off()
            INA_RIGHT.on()
            INB_RIGHT.off()

            # Apply the PWM duty cycle for slowing down
            PWM_LEFT.duty_u16(speed)
            PWM_RIGHT.duty_u16(speed)

            # Print elapsed time
            print(f"Elapsed time for slow down (backward): {elapsed_time:.2f} seconds")
            sleep(0.1)

        # Stop both motors
        PWM_LEFT.duty_u16(0)
        PWM_RIGHT.duty_u16(0)
        INA_LEFT.off()
        INB_LEFT.off()
        INA_RIGHT.off()
        INB_RIGHT.off()

        # Pause between cycles, since I have loop
        sleep(2)

except KeyboardInterrupt:
    # Ensure motors stop if interrupted
    PWM_LEFT.duty_u16(0)
    PWM_RIGHT.duty_u16(0)
    INA_LEFT.off()
    INB_LEFT.off()
    INA_RIGHT.off()
    INB_RIGHT.off()
    print("Program Finished!")
