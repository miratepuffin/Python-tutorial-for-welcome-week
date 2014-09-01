from turtle import * # This tells python to import and use the turtle graphics lib that we will be drawing with

speed(100) # This sets the speed at which the turtle will draw the shape we are going to create, 
		 #a higher number means it will go slower

forward(300) # This function tells the turtle to go forward by a set amount of pixles, given by the number, in this case 300

left(90) 	# This tells the turtle to turn left by a certain amount of degrees given by the number, in this can 90 for a 
			# right angle, we could also use right() if we wanted to turn clockwise

forward(300)
left(90)		

forward(300)
left(90)		

forward(300)
left(90)	# We do this four times as a square has four sides

hideturtle() # We call this method which hides the turtle and allows us to see our shape better
done()	# all turtle graphics must end with a call to the done method to let the computer know when to stop drawing
