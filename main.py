# başlamak için yön tuşu
from turtle import Screen
from snake import Snake
from wall import Wall
from food import Food
from scoreboard import Scoreboard
import time

window = Screen()
window.setup(width = 600, height =600)
window.bgcolor("#497036")
window.title("Snake")
window.tracer(0) # block the animation

# Create the objects
snake = Snake()
wall = Wall()
food = Food()
score = Scoreboard()

difficulty = 0.05 # snake's speed

# control the snake's direction
window.listen()
window.onkey(key = "Up", fun = snake.move_up)
window.onkey(key = "Right", fun = snake.move_right)
window.onkey(key = "Left", fun = snake.move_left)
window.onkey(key = "Down", fun = snake.move_down)

is_game_on = True

while is_game_on:

    window.update()
    time.sleep(difficulty) 

    if snake.press_key: # press the arrow key to start game
        snake.move()

    if snake.collision(): # check the collision
        score.game_over()
        is_game_on = False

    if snake.parts[0].distance(food) < 18:
        food.another_place()

        for part in snake.parts: 
            # if the food is in the snake refresh the food place
            if part.distance(food) < 10:
                food.another_place()

        snake.grow()
        score.plus_score()

        if difficulty > 0.015: 
            # if the snake's speed greater than 0.015, reduce the difficulty when the snake eats
            difficulty -= 0.001



# press 'ESC' to exit at the end of the game
window.onkeypress(window.bye, "Escape")

window.mainloop()