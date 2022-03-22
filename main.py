from turtle import Turtle,Screen


timmy = Turtle()
screen = Screen()
def forward():
    timmy.forward(20)
    return


def back():
    timmy.back(20)
    return

def right():
    timmy.right(90)
    return

def left():
    timmy.left(90)
    return

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    return

screen.listen()
screen.onkey(key = 'w', fun = forward)
screen.onkey(key = 's', fun = back)
screen.onkey(key = 'a', fun = left)
screen.onkey(key = 'd', fun = right)
screen.onkey(key = 'c', fun = clear)










screen.exitonclick()