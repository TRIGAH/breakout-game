from turtle import Turtle
from paddle import Paddle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.goto(0, 0)
        self.dx = 2
        self.dy = -2


    def move(self):      
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    # def y_bounce(self):
    #     self.y_move *= -1

    # def x_bounce(self):
    #     self.x_move *= -1
    #     self.move_speed *= 0.9

    # def resetposition(self):
    #     self.goto(0,0)
    #     self.x_bounce()   
    #     self.move_speed = 0.1 


