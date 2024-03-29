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

    def break_brick(self):
        # Increase score when a brick is broken
        self.score += 10
        self.bricks_broken += 1

    def hit_paddle(self):
        # Increase score when the ball hits the paddle
        self.score += 5

    def lose_life(self):
        # Decrease score when a life is lost
        self.score -= 5

    def get_score(self):
        return self.score

    def update_scoreboard(self):
        self.clear()
        self.goto(0,200)
        self.write(f"{self.get_score()}", align="center", font=("Courier",80,"normal"))
    
    def point(self):
        self.score +=1
        self.update_scoreboard()