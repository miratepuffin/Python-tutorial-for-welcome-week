import random
from turtle import *

speed(35)

bgcolor("Black")
color("White")

r = lambda: random.randint(0,255)

def square(lngth): # method that draws a square
    for i in range(4):
        forward(lngth)
        left(90)

def circle(lngth): # method that draws a circle
    circle(lngth)

def hexagon(lngth): # method that draws a hexagon
    for i in range(6):
        forward(lngth)
        left(60)
        
def rhombus(lngth): # method that draws a rhombus
    forward(lngth)
    left(120)
    forward(lngth)
    left(60)
    forward(lngth) 
    
def triangle(lngth): # method that draws a triangle
    for i in range(3):
        forward(lngth)
        left(120)

def star(lngth):
    angle = [36,144,144,144,144]
    for i in angle:
        left(i)                                             #turn i degree to the left
        forward(lngth)
        
options = {'square': square,
           'circle': circle,
           'hexagon': hexagon,
           'rhombus': rhombus,
           'triangle': triangle,
           'star': star,
} # A python dictionary, defining symbols (keys) and bound methods()

def shape(choice, length): # Check what shape user picked
    if choice in options: # If the shape exists in our dictionary
        options[choice](length) # call the method associated with the symbol and pass length
    else: # else print I dont know that shape
        #print "I dont know that shape!"
        done() # exit program

def rotation(choice, length): # our method that creates the spiral
    n = 0
    c = 1
    transit = False # boolean flag
    colormode(255) # set color mode to RGB
    pencolor((255,0,c)) # start with the color red
    for count in range(512): # loop 512 times, 512 spiral steps
        shape(choice, length) # draw the shape each time
        c += 1 if not transit else -1 # ternary if, increasing the Blue value of the color along the spectrum
        if(c == 255 or c == 0): # if we reach 255 or 0, change direction
            transit = not transit # reverse the boolean flag
        pencolor((255,0,c))
        n += 1 # increase spiral size
        length += 1 # increase shape size
        left(3) # change angle

penup() # lift pen so we dont trace
goto(0,0) # goto coordiantes X and Y
pendown() # set the pen down on paper (figuratively)

choice = input("What shape would you like to draw: ") # prompt user for shape input
length = int(input("Enter a size for your shape: ")) # prompt user for size
rotation(choice, length) # call the method with user input as parameters

hideturtle()
done() # exit program