from turtle import Turtle
import random

# inheritance method below:
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.y_location = random.randint(-275, 275)
        self.x_location = random.randint(-275, 275)
        self.goto(self.x_location, self.y_location)

