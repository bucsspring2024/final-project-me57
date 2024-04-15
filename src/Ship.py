class Ship:
    def __init__(self,x,y,velocity,direction,rotate,img_file):
        """
        Initializes ship object
        args"
            -x=int-current x position
            -y=int-current y position
            -velocity=int-magnitude of velocity,change in x,y position
            -direction=int-where is the front of the ship facing
            -rotate=int-change in direction
        """
        self.position=x,y
        self.img_file=img_file
        self.velocity=velocity
        self.direction=direction
        self.rotate=rotate

    def move_foward(self):
        """
        Updates current position
        """
        self.position+=self.velocity
    def rotate(self):
        """
        Updates current direction
        """
        self.direction+=self.rotate
    def shoot(self,shoot="Flase"):
        """
        Shoots a projectile
        """
        if shoot == True:
            return Beam#Need to create a projectile from ship's coord/direction
