from turtle import Screen, Turtle, position
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

   
level = 10
segments = []
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)        
snake = Snake()
screen.update() 

screen.onkey(fun = snake.turn_north,key ="w")
screen.onkey(fun = snake.turn_west,key ="a")
screen.onkey(fun = snake.turn_south, key = "s")
screen.onkey(fun = snake.turn_east,key ="d")    
screen.listen()

food = Food()
scoreboard = Scoreboard()
while snake.is_game_on():
    screen.update()      
    snake.move()       
    if snake.snake_head.distance(food.food.position()) < 15:
        print("nom nom nom")
        #old food gone
        food.refresh()
        #count for the score
        scoreboard.add_score()
        #add new segment
        #new food in new location
    time.sleep(0.1)

    
screen.exitonclick()
    

    