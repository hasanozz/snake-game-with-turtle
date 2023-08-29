from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-265, 250)
        self.score = -1
        self.plus_score()

    def plus_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}",  align = "center", font=('Courier', 24, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER\n", align = "center", font=('Courier', 30, 'bold'))
        self.goto(0,-30)
        self.write("Press 'ESC' To Exit", align = "center", font=('Courier', 24, 'bold'))

    def reset_scoreboard(self):
        self.clear()
        self.goto(-265, 250)
        self.score = -1
        self.plus_score()