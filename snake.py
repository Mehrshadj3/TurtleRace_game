from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

TURTLE_POS = [(0, 0), (15, 0), (30, 0)]

class Snake():
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]


    def creat_snake(self):
        for item in TURTLE_POS:
            self.add_snake(item)


    def add_snake(self,item):
        turtle = Turtle('square')
        turtle.penup()
        turtle.color('white')
        turtle.goto(item)
        self.segments.append(turtle)

    def extend(self):
        self.add_snake(self.segments[-1].position())

    def move(self):
        for item in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[item - 1].xcor()
            new_y = self.segments[item - 1].ycor()
            self.segments[item].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
         self.head.seth(90)

    def down(self):
       if self.head.heading() != UP:
        self.head.seth(270)

    def left(self):
       if self.head.heading() != RIGHT:
        self.head.seth(180)

    def right(self):
       if self.head.heading() != LEFT:
        self.head.seth(0)




