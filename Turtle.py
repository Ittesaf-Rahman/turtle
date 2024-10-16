import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400, 300)
polygon = turtle.Turtle()
number_of_side = 6
number_of_lenth = 70
number_of_angle = 360 / 6
for i in range(number_of_side):
    polygon.forward(number_of_lenth)
    polygon.right(number_of_angle)
turtle.done()