from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

        # keep the highest score
        with open("high_score.txt") as self.high_score_file: 
            self.content = self.high_score_file.read()
            self.high_score = int(self.content)

        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-265, 250)
        self.write(f"{self.score}",  align = "center", font=('Courier', 24, 'bold'))
        self.goto(0, 250)
        self.write(f"High Score: {self.high_score}",  align = "center", font=('Courier', 24, 'bold'))
        
        
    def increase_score(self):
        # if snake eat the food increase the score by 1 and write this
        self.score += 1
        self.update_score()

    def game_over(self):
        if self.score > self.high_score:
            # compare score with high_score if score is greater than high_score make new high_score is score and change high_score.txt
            with open("high_score.txt", mode = "w") as self.high_score_file:
                self.new_high_score = str(self.score)
                self.high_score_file.write(self.new_high_score)
 
        self.update_score()
        self.goto(0, 0)
        self.write("GAME OVER\n", align = "center", font=('Courier', 30, 'bold'))

        self.goto(0,-30)
        self.write("Press 'ESC' to Exit", align = "center", font=('Courier', 24, 'bold'))

        self.goto(0, -78)
        self.write("Press 'Space' to Play Again", align = "center", font=('Courier', 24, 'bold'))

        