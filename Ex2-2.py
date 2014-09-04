
from turtle import *

color = input("Name a color: ")
user_input = input("Define the radius for your circle: ")
radius = int(user_input)

speed(100)

if(color not in ['blue', 'Blue', 'BLUE']): 
    color = 'red';
    #One of many ways to check if the set color is blue or NOT. Remember python is a case sensitive language so all different combinations have been included.
    #If color is not blue, make sure to set color to RED.

pencolor(color) # Set the color of the drawing
# The function accepts string literals such as "red", "yellow", "blue" but also RGB values.

fillcolor(color) # this function is to set the colour that we will fill the shape with. Again we have picked the same user given input

begin_fill()	# A function that tells python what to fill in

circle(radius) # Make a call to pythons circle function

end_fill()	# Once we have finished drawing the shape we tell python to end the fill, such that we dont fill any other drawings after this line                                     

hideturtle()

done()
