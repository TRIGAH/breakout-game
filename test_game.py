import random
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load sounds
pygame.mixer.init()
hit_sound = pygame.mixer.Sound("hit_sound.wav")
lose_life_sound = pygame.mixer.Sound("lose_life_sound.wav")
game_over_sound = pygame.mixer.Sound("game_over_sound.wav")

# Set up the paddle
paddle_width, paddle_height = 100, 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 50, paddle_width, paddle_height)

# Set up the ball
ball_radius = 10
ball = pygame.Rect(screen_width // 2 - ball_radius // 2, screen_height // 2 - ball_radius // 2, ball_radius, ball_radius)
ball_speed_x, ball_speed_y = 7 * random.choice((1, -1)), 7

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.x += 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= screen_height:
        lose_life_sound.play()
        ball_speed_y *= -1
        ball.x, ball.y = screen_width // 2 - ball_radius // 2, screen_height // 2 - ball_radius // 2
        BreakoutGame().lose_life()

    # Ball collision with paddle
    if ball.colliderect(paddle) and ball_speed_y > 0:
        hit_sound.play()
        ball_speed_y *= -1

    # Clear the screen
    screen.fill(BLACK)

    # Draw the paddle and ball
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, BLUE, ball.center, ball_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
