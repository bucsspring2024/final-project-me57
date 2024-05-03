import DynamicObject
import Beam
from pygame.math import Vector2
from pygmae.transform import rotozoom

class Ship(DynamicObject):
    MANEUVERABILITY=3
    ACCERLATION=.5
    BEAM_SPEED=10
    def rotate(self,clockwise=True):
        sign=1 if clockwise else -1
        angle=self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def accelerate(self):
        self.velocity+=self.direction*self.ACCELERATION
    
    def draw(self,surface):
        angle=self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)


    def shoot(self):
        beam_velocity=self.direction
        beam=Beam(self.position,beam_velocity)
        self.create_beam_callback(beam)
