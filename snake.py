from turtle import *
STARTING_POSITION = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    
    def move(self):
        for snake_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snake_num - 1].xcor()
            new_y = self.snake_segments[snake_num - 1].ycor()
            self.snake_segments[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color('white')
        snake.goto(position)
        self.snake_segments.append(snake)  
    
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)