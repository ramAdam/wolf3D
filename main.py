from pyglet.window import Window
import pyglet
from primitives import Segment, Vector, Point
from view import Fov
import pdb
import math


window = Window(800, 600)
x1, y1 = (400, 300)

# parameters for segment
a = Vector(x1, y1)
length = 100
angle = 45


seg = Segment(a, length, angle)

fieldofview = Fov(a, angle, length)
print(fieldofview.getFov())
nAngle = 45
# seg.rotate(nAngle)


def update(dt):
    global nAngle
    # pdb.set_trace()
    if nAngle == 360:
        nAngle = 45
    
    seg.rotate(nAngle)
    nAngle += 45


@window.event
def on_draw():
    window.clear()
    fieldofview.draw()
    # seg.draw()
    
	

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()
