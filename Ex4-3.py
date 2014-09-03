from turtle import *

def drawSquare(x, y, length):
    goto(x,y)
    down()
    for i in range(4):
        forward(length)
        right(90)
    up()


def drawChessboard(x, y, squaresize):
    fill = True
    for j in range(8):
        for i in range(8):
            x1 = x + i * squaresize
            y1 = y - j * squaresize
            if fill:
                fillcolor('black')
                begin_fill()
                drawSquare(x1, y1, squaresize)
                end_fill()
                fillcolor('white')
            else:
                drawSquare(x1, y1, squaresize)
            fill = not fill
        fill = not fill

speed(50)
up()
drawChessboard(-200, 200, 50)

done()
