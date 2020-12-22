from p5 import *
import random

# red, yellow, blue, white
red = [204, 0, 0]
blue = [0, 0, 204]
white = [255, 255, 255]
yellow = [204, 204, 0]

possible_colours = [red, blue, white, yellow]
time_to_change = 120
window_width =640
window_height = 480

current_text_colour = possible_colours[0]
current_background_colour = possible_colours[1]

def setup():
    size(window_width, window_height)
    #no_stroke()
    background(204, 0, 0)
    zigBlack = create_font("HussarBoldExtended-PARP.otf", 32)
    text_font(zigBlack)    

def draw():
    global time_to_change
    global current_text_colour
    global current_background_colour
    global possible_colours
    #print(frame_count)
    
    if key == "1":
        time_to_change = 60
    elif key == "2":
        time_to_change = 120
    elif key == "3":
        time_to_change = 180
    elif key == "4":
        time_to_change = 240
    elif key == "5":
        time_to_change = 300
    elif key == "6":
        time_to_change = 360

    if (frame_count % time_to_change) == 0:
        #print(f"change {frame_count}, {time_to_change} = {frame_count % time_to_change}")
        text_rand = random.randint(0,len(possible_colours) - 1)
        background_rand = random.randint(0,len(possible_colours) - 1)
        if text_rand == background_rand:
            background_rand = (background_rand + 1) % len(possible_colours)

        current_text_colour = possible_colours[text_rand]
        current_background_colour = possible_colours[background_rand]
  
    background(current_background_colour[0], current_background_colour[1], current_background_colour[2])

    #text_size(64)
    #fill(current_text_colour[0], current_text_colour[1], current_text_colour[2])
    #text_align("CENTER")
    #text("COLOUR", (window_width/2, window_height/2))

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
run(frame_rate=60)

