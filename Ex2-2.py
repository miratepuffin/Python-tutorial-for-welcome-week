from turtle import *

color = input("Name a color: ") # Ask the user for a color
shape = input("Name a shape (Square, Triangle or Circle): ").lower() # Ask the user for a shape and convert the input to all lowercase calling .lower()
measure = 'size' if ((shape == 'square') or (shape == 'triangle')) else 'radius' 
# one line if / else statement, which tells set the variable measure to size if the user input for shape was square or triangle, else set the variable to radius
	
size = int(input("Define the " + measure + " for your " + shape + ": " )) # ask the user for the size / radius for their shape then convert to integer (numbers)

speed(100) # set the speed of the turtle to 100

if(color not in ['blue', 'Blue', 'BLUE']): 
    color = 'red';
    #One of many ways to check if the set color is blue or NOT. Remember python is a case sensitive language so all different combinations have been included.
    #If color is not blue, make sure to set color to RED.

pencolor(color) # Set the color of the drawing
# The function accepts string literals such as "red", "yellow", "blue" but also RGB values.

fillcolor(color) # this function is to set the colour that we will fill the shape with. Again we have picked the same user given input

begin_fill()	# A function that tells python what to fill in

if shape == 'square': # if user entered square do this
	forward(size)
	right(90)
	forward(size)
	right(90)
	forward(size)
	right(90)
	forward(size)
elif shape == 'triangle': # if user entered triangle then do this
	forward(size)
	left(120)
	forward(size)
	left(120)
	forward(size)
elif shape == 'circle': # if user entered circle then do this
	goto(0, size)
	right(360)
else: 
	print("I am sorry but I don't know how to draw a " + shape + ".")

end_fill()	# Once we have finished drawing the shape we tell python to end the fill, such that we dont fill any other drawings after this line                                     
hideturtle()

done()
