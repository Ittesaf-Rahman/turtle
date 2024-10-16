import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(400, 400)
board = turtle.Turtle()

size = 0

while True:
    for i in range(4):
        board.fd(size + 1)
        board.left(90)
        size = size - 5
    size = size + 1