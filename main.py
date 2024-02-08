import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up snake initial position and speed
snake_size = 20
snake_speed = 15
snake = [(width // 2, height // 2)]
snake_direction = (1, 0)

# Set up initial food position
food = (random.randint(0, (width - snake_size) // snake_size) * snake_size,
        random.randint(0, (height - snake_size) // snake_size) * snake_size)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the snake
    x, y = snake[0]
    x += snake_direction[0] * snake_size
    y += snake_direction[1] * snake_size
    snake.insert(0, (x, y))

    # Check for collisions with the walls
    if x < 0 or x >= width or y < 0 or y >= height:
        pygame.quit()
        sys.exit()

    # Check for collision with the food
    if snake[0] == food:
        food = (random.randint(0, (width - snake_size) // snake_size) * snake_size,
                random.randint(0, (height - snake_size) // snake_size) * snake_size)
    else:
        snake.pop()

    # Draw the background
    win.fill(white)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(win, green, (segment[0], segment[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(win, red, (food[0], food[1], snake_size, snake_size))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    pygame.time.Clock().tick(snake_speed)
