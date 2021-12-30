from turtle import Turtle
from scoreboard import Scoreboard

class Snake:
    def __init__(self):
        segments = []
        snake_head = Turtle("triangle")
        snake_head.color("white")
        snake_head.penup()    
        for i in range(0,3):
            new_segment = Turtle("square")
            new_segment.color("red")
            new_segment.penup()
            new_segment.setpos(x = -20*(i+1), y= 0 )
            segments.append(new_segment)  
        self.snake_head = snake_head
        self.segments = segments
     
    def move(self):
        old_position = self.snake_head.position()
        self.snake_head.forward(20)
        for segment in self.segments:
            segment_postion = segment.position()
            segment.goto(old_position)
            old_position = segment_postion
        self.last_segment_position = old_position
    def turn_north(self):
        if self.snake_head.heading() != 270 :
            self.snake_head.setheading(90)
        
    def turn_west(self):
        if self.snake_head.heading()!= 0:
            self.snake_head.setheading(180)
        
    def turn_south(self):
        if self.snake_head.heading()!= 90:
            self.snake_head.setheading(270)
        
    def turn_east(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
        

    def add_body(self):
        print("segments_size: ", len(self.segments))
        new_segment = Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.setposition(self.last_segment_position)
        self.segments.append(new_segment)

    def is_game_on(self):
        xcor = self.snake_head.xcor()
        ycor = self.snake_head.ycor()
        edge = 290
        
        if xcor > edge or xcor < -edge:
            return False
        elif ycor > edge or ycor < -edge:
            return False
        else:
            #print("==========")
            #print("segments_size: ", len(self.segments))                        
            for segment in self.segments:
                print(self.snake_head.position())
                print(segment.position())
                if self.snake_head.distance(segment.position()) < 10:
                    #print("GG")
                    return False
                else:
                    #print("Not yet")
        return True    
        

                   
        


        
                    
            
    
             
