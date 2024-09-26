[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9apGZMRE)
# Motor Test
In this assignment, you'll test the Pico board, the motor driver board and the DC motors.
  
## Requirements:
Complete the Python scripts and answer the questions by editing the [README](/README.md) file. 
### (50%) [ramp_up_down.py](/ramp_up_down.py)
Slowly increase and decrease both motors' speed. Both motors should take actions at the same time.
1. (10%) Ramp up both motors' speed (from stall to max) in 4 seconds. Spin both motors **forward**.
2. (10%) Slow down both motors' speed (from max to stall) in 4 seconds. Spin both motors **forward**.
3. (10%) Ramp up both motors' speed (from stall to max) in 4 seconds. Spin both motors **backward**.
4. (10%) Slow down both motors' speed (from max to stall) in 4 seconds. Spin both motors **backward**.
5. (10%) Stop both motors.
> **Hint**:
> - you may want to refer to the `fade_in_fade_out.py` from your second assignment.
> - No while loop is needed.

### (50%) Estimate Motor Speed
Make marks on both wheels at same spot before you start the testing [script](/estimate_speed.py). Run testing script and observe the motors behaviors carefully.
1. (10%) Complete the testing script: [estimate_speed.py](/estimate_speed.py). Spin both motors on same direction with 50% duty cycle PWM signals. Let the spinning last for 1 minute. Then stop.
> **Hint**: No loop is needed.
2. (30%) Observe the motor's behavior carefully and answer the questions below.
   1. (20%) Can you estimate the speed of each motor using "revolutions per minute (RPM)"? Please round the RPM to **one decimal place**. 
      > ~118.1 RPMs for Right Wheel
      > ~120.8 RPMs for Left Wheel
   2. (10%) What would be the reasons if the speeds of the motors were different? 
      > There are a few different reasons why the motor's speed could be different. The first being that the motors, while they are the same, could have some small differences in the way that they were manufactured. This could cause a chnage in how the motors operate. The next reason being motor age or motor wear, one of the motors could be older than one another, which could cause a decline in motor function. Also, there could be a potential problem with the wiring that connects the motor to the driver and the driver to the Pico. All of these things could influence how the motor operates. 
3. (10%) Upload images to show final location of the marks on each wheel.
   ![Right Motor](https://github.com/user-attachments/assets/ff42f0c3-df2e-4b44-9568-b11776fbe20e)
   ![Left Motor](https://github.com/user-attachments/assets/cd59a07b-cb9d-4833-9ffa-ea4640e6c69b)

   
## AI Usage Policy
Please give credits to your AI assistance. Refer to the [syllabus](https://linzhanguca.github.io/_docs/robotics1-2024/syllabus.pdf) for the citation format.
