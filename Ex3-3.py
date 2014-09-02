from turtle import * 

speed(50) # set the drawing speed to 50, lower = faster

speed = 1 # set a variable called speed to 1
while (speed < 50): # loop until the condition is fulfilled, so if the speed is greater than 50 then stop looping
    forward(speed) # draw forward 1 step
    left(20) # turn 20 degrees
    speed += 0.1 # increase the speed by 0.1 each time we execute
