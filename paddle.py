from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -250)

        # Paddle movement
    def paddle_right(self):
        x = self.xcor()
        if x < 240:
            self.setx(x + 20)

    def paddle_left(self):
        x = self.xcor()
        if x > -240:
            self.setx(x - 20)

