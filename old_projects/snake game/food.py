from turtle import Turtle, Screen
import random
#make a class for food that the snake will eat
class Food(Turtle): #inherit from the turtle class
    def __init__(self):
        super().__init__()
        self.count = 0
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)#make the food smaller
        self.color("yellow")
        self.speed("fastest")
        
        
    def refresh(self):
        random_x = random.randint(-280, 280) #size smaller than the size of the screen on main
        random_y = random.randint(-280, 270)
        self.goto(random_x, random_y)