import time
from turtle import Turtle, Screen
#remember to indent correctly.
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 10
MOVE_INTERVAL = 1000
screen = Screen()
class Snake:
    #create a snake body
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        
        #this to make the snake move by having the screen listen to the key
        screen.listen()
        screen.onkey(self.move_up, "w")
        screen.onkey(self.move_down, "s")
        screen.onkey(self.move_left, "a")
        screen.onkey(self.move_right, "d")
        #create a snake body
    def create_snake(self):
            for position in STARTING_POSITIONS:
                new_snake = Turtle("square")
                new_snake.color("white")
                new_snake.penup() # so it doesn't draw a line
                new_snake.goto(position)
                new_snake.speed("slowest")
                self.snake.append(new_snake)
                    
        #to move the snake
    def move(self):
            for num_snake in range(len(self.snake) -1, 0, -1):
                new_x = self.snake[num_snake - 1].xcor()
                new_y = self.snake[num_snake - 1].ycor()
                self.snake[num_snake].goto(new_x, new_y)
            
            self.head.forward(MOVE_DISTANCE)
            
    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        
                
    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            
    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)              
            