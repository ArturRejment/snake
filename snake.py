from turtle import Turtle, Screen
import time

segments_position = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        
        self.snake_segments = []
        
        for seg in segments_position:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(seg)
            self.snake_segments.append(turtle)    
    
    def move(self):
        for seg_num in range(len(segments_position)-1, 0, -1):
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(x = new_x, y = new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)
        