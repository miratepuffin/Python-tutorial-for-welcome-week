from turtle import *

#Code to write the name Alhamza in turtle graphics

# Draw capital A
penup() # Lift the pen so we dont trace
goto(-200, 0) # Goto the coordinates X and Y
pendown() # Put pen dawn (figuratively on paper)
right(120) # Set the draw direction to 120 degrees away from -> (ie. diagnolly south west)
forward(90) # Draw 90 steps
penup() 
goto(-200,0) # Goto the coordinates X and Y (starting position)
left(60) # Draw a mirror line of the first (ie. diangolly south east)
pendown() 
forward(90) 
penup() 
goto(-175, -45) # Goto the coordiantes X and Y (middle of right line)
right(120) # Change direction to <- (just west)
pendown() 
forward(50)

# Draw a lowercase L
penup()
goto(-140, 0) # increment 15 steps right between letters
pendown()
left(90) # Change direction to south (we previously left at <- so rotate left 90 degrees)
forward(80)
left(90) # Rotate left 90 degrees to go ->
forward(10)

# Lowercase H
penup()
goto(-115, 0)
pendown()
right(90) # Change direction to south (we previously had -> so rotate 90d right)
forward(80)
penup() # again don't trace
goto(-115, -40) # go to the middle of our line
pendown() # start tracing
left(90) # rotate 90 degrees left so we get ->
forward(40)
right(90) # rotate south
forward(40)

# Lowercase A
penup()
goto(-60, -40)
pendown()
left(90) # rotate left 90 degrees we now drawing ->
forward(40)
right(90) # rotate south
forward(20)
right(90) # rotate west
forward(40)
left(90) # rotate south 
forward(20)
left(90) # rotate east
forward(40)
left(90) # rotate north
forward(20)

# Lowercase M
penup()
goto(-5, -40) # *this is first line of m
pendown()
right(180) # rotate south (we previously left facing north)
forward(40)
penup()
goto(-5, -40) # go back to the top of our first line
pendown()
left(90) # rotate east
forward(30)
right(90) # rotate south
forward(40)
penup()
goto(25, -40)
pendown()
left(90) # rotate east
forward(30)
right(90) # rotate south
forward(40)

# Lowercase Z
penup()
goto(70, -40)
pendown()
left(90) # rotate east
forward(40)
goto(70, -80) #diaganolly draw the Z, because we dont use penup() before it will trace
forward(40) #pen still in same direction, dont ahve to use right or left

# Lowercase A (same code as before)
penup()
goto(125, -40)
pendown()
forward(40) # pen still in same direction so we don't need to rotate before
right(90)
forward(20)
right(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)




