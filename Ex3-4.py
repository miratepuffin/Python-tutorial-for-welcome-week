from turtle import *

speed(50) # set the draw speed to 50, lower = faster
distance = 120 # set the distance that we travel to 120
for i in range(50): # loop 50 times, ie. execute the body for 50 times
	forward(distance) # draw forward 120 steps
	left(50) # turn 50 degrees left
done()
