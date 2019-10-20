from pyglet.window import Window
import pyglet
from primitives import Line
import pdb
import math

def rotate(x, y, length, angle):
    
    dx = length * math.cos(math.radians(angle))
    dy = length * math.sin(math.radians(angle))
    return x + dx, y + dy


window = Window(800, 600)
x1, y1 = (400, 300)
x2, y2 = rotate(x1, y1, 100, 90)

cords = (x1, y1, x2, y2)


def update(dt):
   pass

@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
    ('v2f', cords)
    )
    
	

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()
