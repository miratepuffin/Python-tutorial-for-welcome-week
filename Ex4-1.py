from turtle import * 

pencolor('blue') # set the pen color to blue
pensize(5) # increase the pen width to 5
fillcolor('black') # set the fill color to black

def drawRectangle(x, y):
    begin_fill() # fill everything after this point
    for i in range(2): # loop for two times, 0 to 2
        forward(x) # draw forward x steps
        left(90) # turn left 90 degrees
        forward(y) # draw forward y steps
        left(90) # turn left 90 degrees
	# end the for loop, runs twice
    end_fill() # end the fill
		
drawRectangle(80, 40) # make a call to the method that we created which sets x to 20 and y to 10

done()
