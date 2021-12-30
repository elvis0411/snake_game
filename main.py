from turtle import Screen, Turtle
import time

   
level = 10
segments = []
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake_head = Turtle("square")
snake_head.color("white")
snake_head.penup()
        

for i in range(0,3):
    new_segment = Turtle("square")
    new_segment.color("red")
    new_segment.penup()
    new_segment.setpos(x = -20*(i+1), y= 0 )
    segments.append(new_segment)    

screen.update()
time.sleep(1)
   
 
for steps in range(10):
    last_position = snake_head.position()
    snake_head.forward(20)
    for segment in segments:
        segment_position = segment.position()
        segment.goto(last_position)
        last_position = segment_position
    screen.update()
    time.sleep(1/level)
    
        
screen.exitonclick()
    

    