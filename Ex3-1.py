from turtle import *

length = int(input("Please enter a length: ")) # request and length and convert to int

for i in range(0, 4):
# A loop which runs from 0 to 4 (in range), each time saving the current value in the variable i
	forward(length)
	# Move forward X steps, where X is the length given as argument
	right(90)
	# Turn 90 degrees right
# repeat 4 times
	
done()
