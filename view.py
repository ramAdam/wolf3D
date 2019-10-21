from primitives import Segment, anglebtw
import pyglet
import pdb

class Fov:
    
    def __init__(self, origin, angle, length):
        self.angle = angle
        self.origin = origin
        self.rseg = Segment(origin, length, self.angle)
        self.lseg = Segment(origin, length, self.rseg.angle + self.angle)
        

    def draw(self):
        self.rseg.draw()
        self.lseg.draw()

    def getFov(self):
        # pdb.set_trace()
        # return anglebtw(self.rseg.getVectorB(), self.lseg.getVectorB())
        return self.rseg.findAngle(self.lseg)
        