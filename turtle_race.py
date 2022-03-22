from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
bet = False
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle win the race? Enter a color:")
color = ['red','yellow','orange','green','blue','purple']
y_position = [-70,-40,-10,20,50,80]
all_turtles = []

for i in range(0, 6):
    turtles = Turtle(shape='turtle')
    turtles.color(color[i])
    turtles.penup()
    turtles.goto(-230, y_position[i])
    all_turtles.append(turtles)

if user_bet:
    bet = True

while bet:
    for i in all_turtles:
      if i.xcor() > 230:
        bet = False
        win_color = i.pencolor()
        if win_color == user_bet:
            print("You won!")
        else:
            print("You lost!")

      rand = random.randint(0, 10)
      i.forward(rand)















screen.exitonclick()