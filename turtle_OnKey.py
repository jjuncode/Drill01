import turtle

def MoveUp():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def MoveDown():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def MoveLeft():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def MoveRight():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)


def Reset():
    turtle.reset()


turtle.shape('turtle')

turtle.onkey(MoveUp,'w')
turtle.onkey(MoveDown,'s')
turtle.onkey(MoveLeft,'a')
turtle.onkey(MoveRight,'d')

turtle.onkey(Reset, 'Escape')
turtle.listen()

turtle.done()
