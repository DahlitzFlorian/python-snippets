import turtle


turtle.tracer(False)

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()

for i in range(1, 2 ** 16):
    turtle.forward(3)
    if ((i & -i) << 1) & i:
        turtle.lt(90)
    else:
        turtle.rt(90)

turtle.done()
