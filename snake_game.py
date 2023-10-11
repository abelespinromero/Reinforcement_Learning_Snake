
import pygame
import random
import q_learner
from constants import TEXT_COLOR, SNAKE_COLOR , FOOD_COLOR, BACKGROUND_COLOR, BLOCK_SIZE, DIS_WIDTH, DIS_HEIGHT, QVALUES_N, FRAMESPEED


pygame.init()

# Game 

def GameLoop(learner=None):
    global dis
    
    dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    # Starting position of snake
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_list = [(x1,y1)]
    length_of_snake = 1

    # Create first food
    foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    dead = False
    reason = None
    while not dead:
        # Get action from agent
        action = learner.act(snake_list, (foodx,foody))
        if action == "left":
            x1_change = -BLOCK_SIZE
            y1_change = 0
        elif action == "right":
            x1_change = BLOCK_SIZE
            y1_change = 0
        elif action == "up":
            y1_change = -BLOCK_SIZE
            x1_change = 0
        elif action == "down":
            y1_change = BLOCK_SIZE
            x1_change = 0

        # Move snake
        x1 += x1_change
        y1 += y1_change
        snake_head = (x1,y1)
        snake_list.append(snake_head)

        # Check if snake is off screen
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            reason = 'Screen'
            dead = True

        # Check if snake hit tail
        if snake_head in snake_list[:-1]:
            reason = 'Tail'
            dead = True

        # Check if snake ate food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            length_of_snake += 1

        # Delete the last cell since we just added a head for moving, unless we ate a food
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Draw food, snake and update score
        dis.fill(BACKGROUND_COLOR)
        DrawFood(foodx, foody)
        DrawSnake(snake_list)
        DrawScore(length_of_snake - 1)
        pygame.display.update()

        # Update Q Table
        learner.UpdateQValues(reason)
        
        # Next Frame
        clock.tick(FRAMESPEED)

    return length_of_snake - 1, reason

def draw_rounded_rect(surface, color, rect, border_radius):
    """
    Draw a rectangle with rounded corners on a Pygame surface.
    
    Parameters:
        surface (pygame.Surface): The surface to draw on.
        color (tuple): RGB color tuple.
        rect (tuple): The rectangle dimensions (x, y, width, height).
        border_radius (int): The radius of the rounded corners.
    """
    x, y, width, height = rect
    pygame.draw.rect(surface, color, (x + border_radius, y, width - 2 * border_radius, height))
    pygame.draw.rect(surface, color, (x, y + border_radius, width, height - 2 * border_radius))
    pygame.draw.circle(surface, color, (x + border_radius, y + border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + width - border_radius, y + border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + border_radius, y + height - border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + width - border_radius, y + height - border_radius), border_radius)


def DrawFood(foodx, foody):
    draw_rounded_rect(dis, FOOD_COLOR, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE], 5)
    draw_rounded_rect(dis, (0, 0, 0), [foodx + 2, foody + 2, BLOCK_SIZE - 4, BLOCK_SIZE - 4], 3)   

def DrawScore(score):
    font = pygame.font.Font(None, 36)
    value = font.render(f"Score: {score}", True, TEXT_COLOR)
    dis.blit(value, [0, 0])

def DrawSnake(snake_list):
    for x in snake_list:
        draw_rounded_rect(dis, (0, 0, 0), [x[0] + 3, x[1] + 3, BLOCK_SIZE - 6, BLOCK_SIZE - 6], 5)
        draw_rounded_rect(dis, SNAKE_COLOR, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE], 5)



