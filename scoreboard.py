from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.bricks_broken = 0
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.goto(0,0)
        self.write(f"{self.score}", align="center", font=("Courier",80,"normal"))
    
        
    def point(self):
        self.score +=1
        self.update_scoreboard()