import pyglet
from math import cos, sin, radians, sqrt, atan, degrees, acos


def dotproduct(a, b):
    return sum([a.x*b.x, a.y*b.y])

def anglebtw(a, b):
    return degrees(acos(dotproduct(a, b)/ (a.mag() * b.mag())))


class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def mag(self):
        return sqrt(sum([self.x**2, self.y**2]))

    def heading(self):
        """returns the direction of vector"""
        return degrees(atan(self.y/self.x))

    
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y


class Segment:
    def __init__(self, a, length, angle):
        self.a = a
        self.len = length
        self.angle = angle
        self.b = None
        self._calculate()

    def _calculate(self):
        dx = self.len * cos(radians(self.angle))
        dy = self.len * sin(radians(self.angle))
        self.b = Vector(self.a.x + dx, self.a.y + dy)

    def rotate(self, angle):
        self.angle += angle
        self._calculate()    

    def draw(self):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, 
        ('v2f', (self.a.x, self.a.y, self.b.x, self.b.y))
        )

    def getVectorB(self):
        return Vector(self.b.x - self.a.x, self.b.y - self.a.y)

    def findAngle(self, seg):
        """returns a dot product or angle between this segment
           and seg
        """
        pass
        
        