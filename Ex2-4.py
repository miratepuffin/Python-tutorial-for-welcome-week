from turtle import *

shape = input("Would you like to draw a square or a triangle:") #Get the users input for the shape to draw 
colour = input("Would you like that to be red or blue:") #Get the users input for the colour of there first shape
user_input = input("What size would you like it to be?")  #Get the users input for the size of the shape
radius = int(user_input) # Turn the size that the user has entered into a number so that is can be used in calculations
speed(100)

if(shape=="triangle"): #see if they user has chosen to draw a triangle - if so enter this section of code
	if(colour == "red"): # see if they user has chosen the triangle to be red - if so set the fill colour to red
		fillcolor("red")

	elif (colour=="blue"): # if the colour they chose was blue, set the fill colour to blue
		fillcolor("blue")

	else:					# if the colour is neither of these choices then print that the colour is unknown and finish the programme
		print("I am sorry but I don't know that colour")
		done()

	begin_fill() #once the fill colour has been set begin the fill draw the triangle and end the fill
	forward(100)
	left(120)		
	forward(100)
	left(120)		
	forward(100)
	end_fill()

	home()		# We then use the home function to reset the turtles position and angle so that the square isn't at a funky angle
	penup()
	x = xcor()
	y = ycor()		
	x=x-300			
	setpos(x,y) 	
	pendown()	#we then lift the pen up and move to a new position so that the square can be draw sepperatly.

	if(colour == "red"): # we then check the colour again, so that the second shape is the opposite colour to the first
		fillcolor("blue")

	elif (colour=="blue"):
		fillcolor("red")

	begin_fill()	#We then start the fill and draw the square and end the fill
	forward(100)
	left(90)		
	forward(100)
	left(90)		
	forward(100)
	left(90)
	forward(100)
	left(90)   		
	end_fill()	

elif(shape=="square"): # The second part of our outer else if statement checks if the user asked for a square - if so enter the block of code

	if(colour == "red"): #again check what colour the user picked and set the fill colour
		fillcolor("red")

	elif (colour=="blue"):
		fillcolor("blue")

	else:
		print("I am sorry but I don't know that colour")
		done()

	begin_fill()	#This time round as the user has chosen to start with the square we start the fill and draw that first, and then end the fill
	forward(100)
	left(90)		
	forward(100)
	left(90)		
	forward(100)
	left(90)
	forward(100)
	left(90)   		
	end_fill()	

	penup()
	x = xcor()
	y = ycor()		
	x=x-300			# We again move away from the first shape, set the second fill colour and draw the second shape
	setpos(x,y) 	
	pendown()	

	if(colour == "red"):
		fillcolor("blue")

	elif (colour=="blue"):
		fillcolor("red")

	begin_fill()
	forward(100)
	left(120)		
	forward(100)
	left(120)		
	forward(100)
	end_fill()

else:	# The else part of this programme exists as a base case, where if the user enters a shape we don't know then we can tell them via a print out
	print("I am sorry but I don't know how to draw a " + shape + ".")

done()
