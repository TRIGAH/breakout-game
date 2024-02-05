import turtle
from paddle import Paddle
from ball import Ball

ball = Ball()
paddle = Paddle((0,-300))

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle.paddle_right, "Right")
screen.onkeypress(paddle.paddle_left, "Left")

# Main game loop
while True:
    # Move Ball
    ball.move()
    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Paddle interaction
    if (ball.ycor() < -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Game over condition
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    screen.update()
