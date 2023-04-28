from turtle import Turtle, Screen
from food import Food
import time
#make a scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
    def update_score(self):
        self.clear()
        self.score += 1
        
        if self.score > self.high_score:
            self.high_score = self.score
        
            
    def reset_score(self):
        self.score = 0
        
    def show_score(self):
        self.clear()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

        