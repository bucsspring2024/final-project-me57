from pygame.math import Vector2
from Definition import wrap_position
"""
Setup basic information for all interactable and therefore "dynamic objects"
Vector2 is a two dimensional vector, used in this case in velocity and position of any object on the 2D surface
new position is dimensions of coordinate position added to the velocity
"""

class DynamicObject:
    def __init__(self,position,sprite,velocity):
        self.position=Vector2(position)
        self.sprite=sprite
        self.radius=sprite.get_width()/2
        self.velocity=Vector2(velocity)

    def draw(self,surface):
        blit_position=self.position - Vector2(self.radius)
        surface.blit(self.sprtie, blit_position)

    def move(self,surface):
        self.position=wrap_position(self.position + self.velocity,surface)

    def collision(self,other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius