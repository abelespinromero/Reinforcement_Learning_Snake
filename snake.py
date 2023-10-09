import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurar pantalla y colores
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Variables iniciales
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_body = pygame.Surface((10, 10))
snake_body.fill(green)
direction = "RIGHT"
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food = pygame.Surface((10, 10))
food.fill(red)
score = 0

# Configurar fuente y tamaño
font = pygame.font.SysFont("comicsansms", 35)

# Bucle principal del juego
run = True
while run:
    # Eventos y dirección
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            if event.key == pygame.K_DOWN:
                direction = "DOWN"
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                direction = "RIGHT"
                
    # Mover la cabeza de la serpiente
    new_head = list(snake_pos[0])  # Copia de la cabeza actual
    if direction == "UP":
        new_head[1] -= 10
    if direction == "DOWN":
        new_head[1] += 10
    if direction == "LEFT":
        new_head[0] -= 10
    if direction == "RIGHT":
        new_head[0] += 10

    # Insertar nueva cabeza y eliminar última cola
    snake_pos.insert(0, new_head)
    if snake_pos[0] == food_pos:
        score += 1
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    else:
        snake_pos.pop()

    # Si colisiona con los bordes, termina el juego
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
        run = False

    # Si colisiona consigo misma, termina el juego
    if snake_pos[0] in snake_pos[1:]:
        run = False

    # Actualizar la pantalla
    screen.fill(white)
    for pos in snake_pos:
        screen.blit(snake_body, pos)
    screen.blit(food, food_pos)
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [0, 0])

    # Actualizar la ventana del juego
    pygame.display.flip()
    pygame.time.Clock().tick(10)

# Fuera del bucle del juego, terminamos
pygame.quit()
