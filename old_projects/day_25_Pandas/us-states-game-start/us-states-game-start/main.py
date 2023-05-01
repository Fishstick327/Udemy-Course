import os
import pandas as pd
import csv
import turtle

#import the path for the image and the csv file otherwise it will not work
#turtle only accept gif files for some reason
blank_map_img = os.path.join(os.path.dirname(__file__), "blank_states_img.gif")
states_csv = os.path.join(os.path.dirname(__file__), "50_states.csv")


screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("#555555") #aka blackish grey
screen.title("U.S. States Game")
screen.addshape(blank_map_img)
#screen.setup(725, 491)
screen.setup(800, 750)
turtle.shape(blank_map_img)

#find the user input
""" answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer) """

#read the csv file so it can be used in the program
state_data = pd.read_csv(states_csv)
#create a separate list of the state names from the csv file
all_states = state_data.state.to_list()
def total_score(correct_answer):    
        return correct_answer
#match user input with the csv file
#if user_input == csv file, then print the state name on the map
guessed_states = []
correct_answer = 0
game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                              prompt="What's another state's name?")
    
    if answer in state_data["state"].values:
        state_row = state_data[state_data["state"] == answer]
    #find the x and y coordinate of the state from answer_row
        x_coord = state_row['x'].iat[0]    
        y_coord = state_row['y'].iat[0] 
    #[0] is to get the value other wise it return the entire row
        guessed_states.append(answer)
        t.penup()
        t.goto(x_coord, y_coord)
        t.write(answer, align="center", font=("Arial", 8, "normal"))
        t.hideturtle()
        correct_answer += 1
    
    if answer == "exit":
            game_is_on = False
            score = total_score(correct_answer)
            t.screen.textinput(title="Total Score", prompt=f"Your total score is {score}")
            print(score)
            
    
screen.exitonclick()