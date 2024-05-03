import pygame
from Definition import load_sprite
from assets import Asteroid1,Asteroid2,Asteroid3,Background,Ship
import Ship

class Controller:
  
  def __init__(self):
    #setup pygame data
    self._init_pygame()
    self.screen=pygame.display.set_mode((1280,720))
    self.background=load_sprite("Background",False)
    
    self.asteroids=[]
    self.beam=[]
    self.drone=[]
    self.ship=Ship((1280/2,720/2))
    
  def mainloop(self):
    while True:
      self._handle_input()
      self._process_game_logic()
      self._draw()

  def _init_pygame(self):
    pygame.init()
    pygame.display.set_caption("Space Rocks")

  def _handle_input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT or (
        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        quit()
      elif (
        self.spaceship
        and event.type == pygame.KEYDOWN
        and event.key == pygame.K_SPACE
      ):
        self.spaceship.shoot()

    is_key_pressed = pygame.key.get_pressed()

    if self.spaceship:
      if is_key_pressed[pygame.K_RIGHT]:
        self.spaceship.rotate(clockwise=True)
      elif is_key_pressed[pygame.K_LEFT]:
        self.spaceship.rotate(clockwise=False)
      if is_key_pressed[pygame.K_UP]:
        self.spaceship.accelerate()

    def _process_game_logic(self):
      for game_object in self._get_game_objects():
        game_object.move(self.screen)

      if self.spaceship:
        for asteroid in self.asteroids:
          if asteroid.collides_with(self.spaceship):
            self.spaceship = None
            self.message = "You lost!"
            break

      for beam in self.beam[:]:
        for asteroid in self.asteroids[:]:
          if asteroid.collides_with(bullet):
            self.asteroids.remove(asteroid)
            self.bullets.remove(bullet)
            asteroid.split()
            break

        for bullet in self.bullets[:]:
          if not self.screen.get_rect().collidepoint(bullet.position):
            self.bullets.remove(bullet)

        if not self.asteroids and self.spaceship:
            self.message = "You won!"

    def _draw(self):
      self.screen.blit(self.background, (0, 0))

      for game_object in self._get_game_objects():
        game_object.draw(self.screen)


      pygame.display.flip()
      self.clock.tick(60)

    def _get_game_objects(self):
      game_objects = [*self.asteroids, *self.bullets]

      if self.spaceship:
        game_objects.append(self.spaceship)

      return game_objects