import time
from turtle import *

screensize(1024,768)
bgcolor("red")
time.sleep(3)
clearscreen()
time.sleep(1)
bgpic("background.gif")

pensize(4)
penup()
goto(-10, 220)
pendown()

for i in range(2):
	forward(150)
	right(90)
	forward(100)
	right(90)

penup()
goto(-10, 170)
pendown()
right(180)
forward(50)

right(180)
penup()
goto(-210, 180)
pendown()

for j in range(2):
        forward(150)
        right(90)
        forward(100)
        right(90)

done()
