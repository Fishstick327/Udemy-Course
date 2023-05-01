from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

food = Food()
scoreboard = Scoreboard()
snake = Snake()
 #when importing from another class the structure is overlapping with the original class
    #so make sure to change the structure of the imported class to match the original class
    #make a copy if you need to
def game_over():
    print("GAME OVER")
    time.sleep(2)
    game_over_t = Turtle()
    game_over_t.penup()
    game_over_t.color("white")
    game_over_t.goto(0, 0)
    reset_score = scoreboard.reset_score()
    game_over_t.write("GAME OVER", align="center", font=("Arial", 25, "normal"))
    game_over_t.clear()
    screen.update()
    snake.reset()
    game_over_t.hideturtle()
    


game_is_on = True
while game_is_on:    #while loop is on update the screen every 0.1 second
    screen.update()
    time.sleep(0.1)
        
    snake.move() #call the move function from the snake class base on the move function
    
    #detect collision with food and +1 to the scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        create_snake = snake.create_snake()
        increase_score = scoreboard.increase_score()
        update_score = scoreboard.update_score()
        
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_over()
        
        
        
    
    
screen.exitonclick()