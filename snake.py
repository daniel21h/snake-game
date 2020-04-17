import pygame, random
from pygame.locals import *

# Alinhamento da cobra com a uva
def on_grid_random():
  x = random.randint(0, 590)
  y = random.randint(0, 590)
  return (x // 10 * 10, y // 10 * 10)

# Testando colisão entre duas células
def collision(c1, c2):
  return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Definição de macro para o movimento da cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0, 255, 0))

grape_pos = on_grid_random()
grape = pygame.Surface((10, 10))
grape.fill((255, 0, 0))

my_direction = LEFT

# Limitando FPS
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while True:
  clock.tick(15)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()

    # Controlando a cobra
    if event.type == KEYDOWN:
      if event.key == K_UP:
        my_direction = UP
      if event.key == K_DOWN:
        my_direction = DOWN
      if event.key == K_RIGHT:
        my_direction = RIGHT
      if event.key == K_LEFT:
        my_direction = LEFT

  if collision(snake[0], grape_pos):
    grape_pos = on_grid_random()
    snake.append((0, 0))
    score = score + 1

  # Verifique se a cobra colidiu com os limites
  if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
    game_over = True
    break
  
  # Verifique se a cobra atingiu a si mesma
  for i in range(1, len(snake) -1):
    if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
      game_over = True
      break

  if game_over:
    break

  for i in range(len(snake) -1, 0, -1):
    snake[i] = (snake[i-1][0], snake[i-1][1])

  # Fazendo a cobra se mover
  if my_direction == UP:
    snake[0] = (snake[0][0], snake[0][1] - 10)
  if my_direction == DOWN:
    snake[0] = (snake[0][0], snake[0][1] + 10)
  if my_direction == RIGHT:
    snake[0] = (snake[0][0] + 10, snake[0][1])
  if my_direction == LEFT:
    snake[0] = (snake[0][0] - 10, snake[0][1])

  screen.fill((0, 0, 0))
  screen.blit(grape, grape_pos)

  for x in range(0, 600, 10): # Desenhar linhas verticais
    pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
  for y in range(0, 600, 10): # Desenhar linhas verticais
    pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

  score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
  score_rect = score_font.get_rect()
  score_rect.topleft = (600 - 120, 10)
  screen.blit(score_font, score_rect)

  for pos in snake:
    screen.blit(snake_skin, pos)

  pygame.display.update()

while True:
  game_over_font = pygame.font.Font('freesansbold.ttf', 75)
  game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
  game_over_rect = game_over_screen.get_rect()
  game_over_rect.midtop = (600 / 2, 10)
  screen.blit(game_over_screen, game_over_rect)
  pygame.display.update()
  pygame.time.wait(500)

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()