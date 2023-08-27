from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
STEPS = 20

class Snake():

    def __init__(self):
        self.parts = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_part = Turtle("square")
            self.parts.append(new_part)
            self.parts[i].penup()
            self.parts[i].goto(STARTING_POSITIONS[i])

    def move(self):
        for i in range(len(self.parts) -1 , 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.parts[0].fd(STEPS)


    def game_over(self):
        if self.parts[0].xcor() >= 290 or self.parts[0].xcor() <= -300 or self.parts[0].ycor() >= 300 or self.parts[0].ycor() <= -290:
            return True
        
    def move_up(self):
        if self.parts[0].heading() != 270:
            self.parts[0].setheading(90)
            

    def move_right(self):
        if self.parts[0].heading() != 180:
            self.parts[0].setheading(0)
            

    def move_left(self):
        if self.parts[0].heading() != 0:
            self.parts[0].setheading(180)  
              

    def move_down(self):
        if self.parts[0].heading() != 90:
            self.parts[0].setheading(270)
            