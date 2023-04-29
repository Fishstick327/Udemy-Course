from turtle import Turtle, Screen
from food import Food
import time
#make a scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data_score.txt", mode="r") as data_score:
            self.high_score = int(data_score.read()) 
            #this read the int value of high score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()   
        self.update_score()
       
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
        if self.score > self.high_score:
            self.high_score = self.score    
            #function to write the highest score into a text file and save it
            with open("data_score.txt", mode ="w") as data_score:
                print("score saved")
                data_score.write(f"{self.high_score}") #but when it write it need to be a string
                print("finished")
                data_score.close()
                print("closed")   
    def reset_score(self):
        self.score = 0
        self.update_score()
        
        
    def increase_score(self):
        self.score += 1
        self.update_score()
       
        