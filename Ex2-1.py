
from turtle import *

user_input = input("Define the radius for your circle: ") # Call the input function which allows the user to input a value into the terminal
# The string (sentance) that is given to the function is the message promt that allows the user to see what they should be entering. 
# We set a variable called user_input to = what the user typed in so that we can panipulate it and use it in our programme

radius = int(user_input) # the int function is used to change the users input (which was from phythons point of view a word) to a number which
# can have calculations performed upon it. This is again saved into a variable so we can use it later on.

speed(100)

circle(radius) # Make a call to pythons circle function, this draws a full circle with a radius of the number given to it. In this case we use
# the radius that the user entered, but any number would work.

hideturtle()

done()
