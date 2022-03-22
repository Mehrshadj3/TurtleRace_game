from turtle import Turtle




class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 272)
        self.write(f'SCORE: {self.score}', align='center', font=('arial', 20, 'bold'))
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f'SCORE: {self.score}', align='center', font=('arial', 20, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER!', align='center', font=('arial', 20, 'bold'))







