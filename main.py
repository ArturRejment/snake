from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)  # Disable the automate refreshing

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Screen is listening for the keys to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake_head = snake.snake_segments[0]

    # Detect colision with food
    if snake_head.distance(food) < 15:
        food.move_food()
        snake.extend_snake()
        scoreboard.write_score()

    # Detect collision with wall
    if snake_head.xcor() > 280 or snake_head.xcor() < -280 or snake_head.ycor() > 280 or snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tale
    # Slice the list of segments to cut the head
    for segment in snake.snake_segments[1:]:
        if snake_head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
