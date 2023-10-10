
import pygame
import random

def play_game(q_learner=None):
    pygame.init()
    
    width, height = 400, 300
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
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if q_learner:
            direction = q_learner.select_action(snake_pos, food_pos)

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
        
        reward = 0
        
        if snake_pos[0] == food_pos:
            score += 1
            reward = 10
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        else:
            snake_pos.pop()
            reward = -1
            
        if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
            reward = -10
            if q_learner:
                q_learner.update_q_values(old_snake=snake_pos[1:], old_food=food_pos, action=direction, reward=reward, new_snake=None, new_food=None)
            return score
            
        if snake_pos[0] in snake_pos[1:]:
            reward = -10
            if q_learner:
                q_learner.update_q_values(old_snake=snake_pos[1:], old_food=food_pos, action=direction, reward=reward, new_snake=None, new_food=None)
            return score
            
        if q_learner:
            q_learner.update_q_values(old_snake=snake_pos[1:], old_food=food_pos, action=direction, reward=reward, new_snake=snake_pos, new_food=food_pos)
        
        # Drawing logic
        screen.fill(white)
        for pos in snake_pos:
            screen.blit(snake_body, pos)
        screen.blit(food, food_pos)
        score_text = font.render("Score: " + str(score), True, black)
        screen.blit(score_text, [0, 0])
        
        pygame.display.flip()
        pygame.time.Clock().tick(30)
