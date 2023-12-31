from turtle import Screen
from snake import Snake
from wall import Wall
from food import Food
from scoreboard import Scoreboard
import time

# Create the window and set the resolution
window = Screen()
window.setup(width = 600, height = 600)

def again():
    # clear the window and call the game method
    window.clear()
    game()

def game():
    # set the window background color and give name the window title
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

    is_game_active = True
    while is_game_active:

        window.update()
        time.sleep(difficulty) 

        if snake.press_key: # press 'Up', 'Down' or 'Right' arrow key to start the game
            snake.move()

        if snake.collision(): # check the collision
            is_game_active = False
            score.game_over()

            window.onkey(key = "space", fun = again) # if the player press 'space' refresh the game
            window.onkeypress(key = "Escape", fun = window.bye) # if the player press 'esc' exit the game
            window.mainloop()

        if snake.parts[0].distance(food) < 18:
            food.another_place()

            for part in snake.parts: 
                # if the food is in the snake refresh the food place
                if part.distance(food) < 10:
                    food.another_place()

            snake.grow()
            score.increase_score()

            if difficulty > 0.015: 
                # if the snake's speed greater than 0.015, reduce the difficulty when the snake eats
                difficulty -= 0.001

game()