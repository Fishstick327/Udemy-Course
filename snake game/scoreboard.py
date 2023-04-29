from turtle import Turtle, Screen
from food import Food
import time
import os
#make a scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #the os.path.dirname(__file__) is to get the path of current folder and join it with the file name
        file_path = os.path.join(os.path.dirname(__file__), "data_score.txt")
        self.score = 0
        #file_path = r"C:\Users\natha\Desktop\WEd Development  bootcamp\Udemy Code\snake game\data_score.txt"
        with open(file_path, mode="r") as data_score:
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
            
            file_path = os.path.join(os.path.dirname(__file__), "data_score.txt")
            with open(file_path, mode ="w") as data_score:
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
       
        