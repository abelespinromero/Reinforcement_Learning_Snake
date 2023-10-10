
import pygame
import random
import numpy as np

def play_game(q_learning=False, action=None):
    pygame.init()
    
    # Configurations
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    
    snake_pos = [[100, 50], [90, 50], [80, 50]]
    snake_body = pygame.Surface((10, 10))
    snake_body.fill(green)
    direction = "RIGHT"
    
    food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food = pygame.Surface((10, 10))
    food.fill(red)
    
    score = 0
    font = pygame.font.SysFont("comicsansms", 35)
    
    if q_learning:
        if action:
            direction = action

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = "UP"
                if event.key == pygame.K_DOWN:
                    direction = "DOWN"
                if event.key == pygame.K_LEFT:
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                    
        new_head = list(snake_pos[0])
        
        if direction == "UP":
            new_head[1] -= 10
        if direction == "DOWN":
            new_head[1] += 10
        if direction == "LEFT":
            new_head[0] -= 10
        if direction == "RIGHT":
            new_head[0] += 10

        snake_pos.insert(0, new_head)
        
        reward = 0  # Initialize reward
        
        if snake_pos[0] == food_pos:
            score += 1
            reward = 10  # Positive reward for eating the food
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        else:
            snake_pos.pop()
            reward = -1  # Negative reward for not eating the food
            
        if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
            reward = -10  # Negative reward for dying
            return None, reward, True  # State is None, Game Over
            
        if snake_pos[0] in snake_pos[1:]:
            reward = -10  # Negative reward for dying
            return None, reward, True  # State is None, Game Over
            
        screen.fill(white)
        for pos in snake_pos:
            screen.blit(snake_body, pos)
        screen.blit(food, food_pos)
        score_text = font.render("Score: " + str(score), True, black)
        screen.blit(score_text, [0, 0])
        
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        
        if q_learning:
            # Calculate state features: distance and angle to the food
            dx = food_pos[0] - snake_pos[0][0]
            dy = food_pos[1] - snake_pos[0][1]
            angle = np.arctan2(dy, dx)
            distance = np.sqrt(dx**2 + dy**2)
            state = [distance, angle]
            return state, reward, False  # State is distance and angle to the food, Game is not over

if __name__ == "__main__":
    play_game()
