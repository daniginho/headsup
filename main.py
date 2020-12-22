from p5 import *
import random

# red, yellow, blue, white
red = [204, 0, 0]
blue = [0, 0, 204]
white = [255, 255, 255]
yellow = [204, 204, 0]

possible_colours = [red, blue, white, yellow]

def setup():
    size(640, 480)
    #no_stroke()
    background(204, 0, 0)

def draw():
    #print(frame_count)
    #random_colour = random.randint(0,3)
    #colour = possible_colours[0]

    colour = possible_colours[int((frame_count / 300) % len(possible_colours))]

    #if mouse_is_pressed:
    #    colour = possible_colours[random_colour]
    
    background(colour[0], colour[1], colour[2])
    #if mouse_is_pressed:
    #    fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    #else:
    #    fill(255, 15)

    #circle_size = random_uniform(low=10, high=80)

    #circle((mouse_x, mouse_y), circle_size)


def key_pressed(event):
    #background(204)
    pass

#run(frame_rate=1)
run()

