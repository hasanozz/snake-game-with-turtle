from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("#b60000")
        self.speed("fastest")
        self.another_place()

    def another_place(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))