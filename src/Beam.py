import DynamicObject
from Definition import load_sprite
"""

"""

class Beam(DynamicObject):
    def __init__(self,position,velocity):
        super().__init__(position,load_sprite("Beam"),velocity)
    
    def move(self, surface):
        self.position = self.position + self.velocity