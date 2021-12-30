from turtle import Turtle
import random

class Food():
    
    def __init__(self):
        xcor = random.randrange(-250,250)
        ycor = random.randrange(-250,250)
        food = Turtle("circle")
        food.color("blue")
        food.penup()
        food.shapesize(0.5,0.5)
        food.setposition(xcor,ycor)
        self.food = food
        print(self.food.position())
    
    def refresh(self):
        xcor = random.randrange(-250,250)
        ycor = random.randrange(-250,250)
        self.food.setposition(xcor,ycor)
        print(self.food.position())        
        
        
        