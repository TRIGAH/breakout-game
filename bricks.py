from turtle import Turtle

class Brick(Turtle):
    BRICKS = []

    def __init__(self):
            super().__init__()
            self.shape("square")
            self.color('black')
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.penup()
            self.colors = ["red", "orange", "yellow", "green", "blue"]
            self.y_position = 200


    def create_bricks(self):
            for color in self.colors:
                for _ in range(6):
                    brick = Brick()
                    brick.color(color)
                    brick.goto(-250 + 80 * _, self.y_position)
                    self.BRICKS.append(brick)
                
                self.y_position -= 30
        

