from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEPS = 20

class Snake():

    def __init__(self):
        self.press_key = False # have to press arrow key to start
        self.parts = [] # snake's segments list
        self.create_snake()

    def create_snake(self):
        # create the 3 segments snake
        for pos in STARTING_POSITIONS:
            self.add_part(pos)

    def add_part(self, position):
        # if eat the food add a segment to snake
        new_part = Turtle("square")
        new_part.penup()
        new_part.goto(position)
        self.parts.append(new_part)


    def move(self):
        # movement of snake
        for i in range(len(self.parts) -1 , 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.parts[0].fd(STEPS)


    def grow(self):
        self.add_part(self.parts[-1].position())


    def collision(self):
        # if the snake hits the wall or hits the own tail it's game over
        if self.parts[0].xcor() >= 290 or self.parts[0].xcor() <= -300 or self.parts[0].ycor() >= 300 or self.parts[0].ycor() <= -290:
            return True
        for part in self.parts[1:]:
            if self.parts[0].distance(part) < 10:
                return True
        
    def move_up(self):
        if self.parts[0].heading() != 270:
            self.parts[0].setheading(90)
        self.press_key = True
            
    def move_right(self):
        if self.parts[0].heading() != 180:
            self.parts[0].setheading(0)
            self.press_key = True
            

    def move_left(self):
        if self.parts[0].heading() != 0:
            self.parts[0].setheading(180)  
            self.press_key = True


    def move_down(self):
        if self.parts[0].heading() != 90:
            self.parts[0].setheading(270)
            self.press_key = True