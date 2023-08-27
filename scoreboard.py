from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = -1
        self.plus_score()

    def plus_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align = "center", font=('Courier', 14, 'bold'))


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align = "center", font=('Courier', 24, 'bold'))