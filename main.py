from turtle import Screen, Turtle
import time

from snake import Snake

   
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


while snake.is_game_on():
    screen.update() 
    screen.listen() 
    snake.move()       
    time.sleep(0.1)

    
screen.exitonclick()
    

    