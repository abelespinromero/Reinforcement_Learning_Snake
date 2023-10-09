import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Configurar colores
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Inicializar la serpiente y la comida
snake_pos = [[100, 50],
             [90, 50],
             [80, 50]]
snake_body = pygame.Surface((10, 10))
snake_body.fill(green)

food_pos = [random.randrange(1, (width//10)) * 10,
            random.randrange(1, (height//10)) * 10]
food = pygame.Surface((10, 10))
food.fill(red)

# Configurar dirección inicial
direction = 'RIGHT'

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
    
    # Mover la serpiente
    if direction == 'UP':
        snake_pos[0][1] -= 10
    if direction == 'DOWN':
        snake_pos[0][1] += 10
    if direction == 'LEFT':
        snake_pos[0][0] -= 10
    if direction == 'RIGHT':
        snake_pos[0][0] += 10

    # Dibujar la serpiente
    for pos in snake_pos:
        screen.blit(snake_body, pos)
    
    # Dibujar la comida
    screen.blit(food, food_pos)
    
    pygame.display.flip()
    
    # Limpiar la pantalla para el siguiente frame
    screen.fill(white)
    
    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)

pygame.quit()
