from turtle import Turtle
import random

COLOR_LIST = ['green', 'yellow', 'red', 'purple', 'orange']
SHAPE_LIST = ['circle', 'turtle', 'triangle']

""" A class of food for the snake """


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.move_food()

    # A function to move the food to the random position on the screen
    def move_food(self):
        color = random.choice(COLOR_LIST)
        shape = random.choice(SHAPE_LIST)
        self.color(color)
        self.shape(shape)
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
