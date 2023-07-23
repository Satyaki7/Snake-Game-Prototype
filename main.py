# First game 
import pygame,sys
from pygame.math import Vector2

class FRUIT: 
  def _init_(self):
    self.x = 5
    self.y = 4
    self.pos = Vector2(self.x,self.y)
    #creat an x and y position 
    #draw a square 
 
  def draw_fruit(self):
    fruit_rect = pygame.Rect(self.pos.x,self.pos.y,cell_size,cell_size)
    pygame.draw.rect(screen,pygame.Color('red'),fruit_rect)

pygame.init()
#main display
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()

while True: 
  #draw all elements 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  # screen.fill(pygame.Color('gold'))  <--- fixed color 
  screen.fill((172,215,70))
  fruit.draw_fruit()
  
  pygame.display.update()
  clock.tick(60) #frame rate <---- this is the max
  