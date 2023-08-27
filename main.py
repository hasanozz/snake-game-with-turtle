# time modülü ile zorluk seçimi?

from turtle import Screen
from snake import Snake
from wall import Wall
import time

window = Screen()
window.setup(width = 600, height =600)
window.bgcolor("#497036")
window.title("Snake v23")
window.tracer(0)

snake = Snake()
wall = Wall()

window.listen()
window.onkey(key = "Up", fun = snake.move_up)
window.onkey(key = "Right", fun = snake.move_right)
window.onkey(key = "Left", fun = snake.move_left)
window.onkey(key = "Down", fun = snake.move_down)

is_game_on = True

while is_game_on:

    window.update()
    time.sleep(0.1) 

    snake.move()
    if snake.game_over():
        is_game_on = False

window.exitonclick()