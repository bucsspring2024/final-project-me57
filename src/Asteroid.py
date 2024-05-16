import DynamicObject
from pygmae.transform import rotozoom
from Definition import load_sprite, get_random_velocity
"""
pygame.transform.rotozoom() allows for the rotation of 32 bit images
asteroid callback allows for the saving of the image
Asteroid 1 in currently used
"""
class Asteroid(DynamicObject):
    def __init__(self, position, create_asteroid_callback, size=3):
        self.create_asteroid_callback = create_asteroid_callback
        self.size = size

        size_to_scale = {3: 1.0, 2: 0.5, 1: 0.25}
        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite("Asteroid1"), 0, scale)

        super().__init__(position, sprite, get_random_velocity(1, 3))
