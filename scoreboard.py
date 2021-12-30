from turtle import Turtle
class Scoreboard:
    def __init__(self):
        scoreboard = Turtle()
        scoreboard.color("white")
        scoreboard.hideturtle()
        scoreboard.penup()
        scoreboard.setposition(x=0,y= 280)
        scoreboard.pendown()
        self.scoreboard = scoreboard
        self.score = 0
        self.scoreboard.write(f"Score: {self.score}", align = "center",font=15)
        
    def add_score(self):     
        self.scoreboard.pendown()   
        self.score += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align = "center",font=15)