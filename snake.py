from turtle import Turtle, Screen
import time

segments_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

""" A snake class """


class Snake:

    def __init__(self):

        self.snake_segments = []

        for seg in segments_position:
            self.create_segment(seg)

    # Create a new snake segment and add it to the list
    def create_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.snake_segments.append(turtle)

    # Move the snake
    def move(self):
        for seg_num in range(len(self.snake_segments)-1, 0, -1):
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(x=new_x, y=new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    # Add a new segment to the snake
    def extend_snake(self):
        self.create_segment(self.snake_segments[-1].position())

    # Functions to change the snake direction
    def up(self):
        current_heading = self.snake_segments[0].heading()
        if current_heading != 270:
            self.snake_segments[0].setheading(90)

    def down(self):
        current_heading = self.snake_segments[0].heading()
        if current_heading != 90:
            self.snake_segments[0].setheading(270)

    def left(self):
        current_heading = self.snake_segments[0].heading()
        if current_heading != 0:
            self.snake_segments[0].setheading(180)

    def right(self):
        current_heading = self.snake_segments[0].heading()
        if current_heading != 180:
            self.snake_segments[0].setheading(0)
