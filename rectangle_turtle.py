import turtle

turtle.Screen().bgcolor("light pink")
turtle.Screen().setup(300,400)
rectangle = turtle.Turtle()

num_side = 4

for i in range(num_side):
    rectangle.forward(100)
    rectangle.right(90)

turtle.done()