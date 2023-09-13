import turtle

def MoveDir(dir):
    turtle.stamp()
    turtle.setheading(dir)
    turtle.forward(50)

def Reset():
    turtle.reset()

up,down,left,right = 90,270,180,0

turtle.shape('turtle')

turtle.onkey(MoveDir(up),'w')
turtle.onkey(MoveDir(down),'s')
turtle.onkey(MoveDir(left),'a')
turtle.onkey(MoveDir(right),'d')

turtle.listen()

turtle.done()