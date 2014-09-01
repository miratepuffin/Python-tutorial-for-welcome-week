from turtle import * 
speed(100)
pencolor("red") # We can set the colour that the turtle draws with this function, it can take strings of well known colors
				# such as "red", "Yellow", "blue" or if you wanted to be more spesific you can give it RGB values which can
				# be seen in the next colour changes below

fillcolor("#33cc3b") # this function is to set the colour that we will fill the shape with, we can write the colour in hexdecimal
					 # which you may have seen if you have used photoshop or an equivilant programme

begin_fill()	# at the start of drawing the shape that we want to fill we type begin_fill() so that python knows where we want to 
				# colour, we then draw our square
forward(100)
left(90)		

forward(100)
left(90)		

forward(100)
left(90)

forward(100)
left(90)   		

end_fill()		# Once we have finished drawing the shape we are going to fill we type end_fill() so that python can fill the shape
				
penup() 		# When we have finished drawing the first shape, we lift the pen off the canvas so we can move without drawing
				# so that we can move to where we will draw the second shape without drawing a line

x = xcor()
y = ycor()		# We get the current position of the turtles x,y cordinents from the xcor() and ycor() methods
				# We set two varibles to the numbers returned so that we can edit them

x=x-300			# We set the x to 300 less that it was so that it is well out the way of the first shape

setpos(x,y) 	# We now set the turtle to its new position using the setpos() function, giving it the x and y values we have just
				# made

pendown()		#We can now put the pen back down and start drawing again

fillcolor("#ffff00") 
begin_fill()
forward(100)
left(120)		

forward(100)
left(120)		

forward(100)
  # This time I am going to draw a triangle, the angles might seema  bit wierd, but try to visualise it in your head so that if
  # you were the turtle how many degrees left or right would you have to turn to draw the shape

end_fill()
	
hideturtle()
done() 








