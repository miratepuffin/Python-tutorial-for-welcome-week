import time # needed for making the program wait, check bottom
from turtle import *

pencolor('blue') # set the pen color to blue
pensize(5) # increase the pen width to 5

def drawRectangle(x, y, color='yellow'): # the color = 'yellow' part says that if the user gives his own parameter, then change the value to user input, else
# let the standard value be 'yellow'
        fillcolor(color) # set the fill color to what the user defind
        begin_fill() # fill everything after this point
        for i in range(2): # loop for two times, 0 to 2
                forward(x) # draw forward x steps
                left(90) # turn left 90 degrees
                forward(y) # draw forward y steps
                left(90) # turn left 90 degrees
	# end the for loop, runs twice
        end_fill() # end the fill
		
# make a call to the method that we created which sets x to 20 and y to 10
drawRectangle(80, 40) # notice here we wont give a 3rd parameter, so the fill color should be yellow.
time.sleep(3) # wait 3 seconds til we call the second method
drawRectangle(80, 40, 'blue') # here however we give the color blue, so the fill color should be blue.
