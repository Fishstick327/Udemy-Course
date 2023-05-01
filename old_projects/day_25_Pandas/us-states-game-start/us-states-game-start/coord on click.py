import turtle
import pandas as pd
import os
 #this is to get the x, y coordinate of the mouse click and export into a CSV file
 #you can change the format of the dataframe so that is easier to read
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
state_coord = []

def get_mouse_click_coord(x, y):
    print(x, y)
    
    #append the (x, y) not the get_mouse_click_coord otherwise it record the wrong info
    state_coord.append((x, y))
turtle.onscreenclick(get_mouse_click_coord)
turtle.mainloop()
    
