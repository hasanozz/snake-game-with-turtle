# time modülü ile zorluk seçimi?
# duvarın diğer tarafından geçme
# 2 kare büyülten büyük yemek
# dönerken içinden geçmesin
# yiyecek kendi içinde çıkmasın
# tekrar oynamak ister misin?

from turtle import Screen
from snake import Snake
from wall import Wall
from food import Food
from scoreboard import Scoreboard
import time

window = Screen()
window.setup(width = 600, height =600)
window.bgcolor("#497036")
window.title("Snake v23")
window.tracer(0)

snake = Snake()
wall = Wall()
food = Food()
score = Scoreboard()

window.listen()
window.onkey(key = "Up", fun = snake.move_up)
window.onkey(key = "Right", fun = snake.move_right)
window.onkey(key = "Left", fun = snake.move_left)
window.onkey(key = "Down", fun = snake.move_down)

is_game_on = True

while is_game_on:

    window.update()
    time.sleep(0.03) 

    snake.move()

    if snake.parts[0].distance(food) < 18:
        food.another_place()
        snake.grow()
        score.plus_score()

    if snake.game_over():
        score.game_over()
        is_game_on = False

window.exitonclick()