from turtle import *

user_input = input("Enter a size for the outer square: ") # prompt the user to enter a size in the standard command line
size = int(user_input)# convert the user input to integer (numbers) from string literals (words), such that we can preform calculations on the number

while(size > 4):
	#Below we will utilize the same piece of code as the previous exercise, to draw a square using loops
	#Alternatively we can use the python method turtle.square(size)
	for i in range(0, 4):
	# A loop which runs from 0 to 4 (in range), each time saving the current value in the variable i
		forward(size)
		# Move forward X steps, where X is the length given as argument
		right(90)
		# Turn 90 degrees right
	# for loop ends here, repeat 4 times
	size -= 5 # decrease the size by 5
# while loops ends here, repeat until the size is 4 or once if size is less than 4
	
done()
