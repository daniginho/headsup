from p5 import *
import random

window_width =1000
window_height = 670

font_size= 6
zero = [
    [0,0,1,1,1,0],
    [0,1,0,0,0,1],
    [0,1,0,0,0,1],
    [0,1,0,0,0,1],
    [0,1,0,0,0,1],
    [0,0,1,1,1,0],
]
one = [  
    [0,0,1,1,0,0],
    [0,1,1,1,0,0],
    [0,0,1,1,0,0],
    [0,0,1,1,0,0],
    [0,0,1,1,0,0],
    [0,1,1,1,1,0],
]
two = [
    [0,1,1,1,0,0],
    [1,1,0,0,1,0],
    [0,0,0,0,1,0],
    [0,0,1,1,0,0],
    [0,1,0,0,0,0],
    [1,1,1,1,1,0],
]
three =  [
    [0,1,1,1,0,0],
    [1,1,0,0,1,0],
    [0,0,0,1,0,0],
    [0,0,0,1,1,0],
    [1,1,0,0,1,0],
    [0,1,1,1,0,0],
]


red = [204, 0, 0]
blue = [0, 0, 204]
white = [255, 255, 255]
yellow = [204, 204, 0]

possible_colours = [red, blue, white, yellow]

time_to_change = 120

current_text_colour = possible_colours[0]
current_background_colour = possible_colours[1]
box_size = 45

box_x = (window_width/2)-(box_size* (font_size/2))
box_y = (window_height/2)-(box_size* (font_size/2))
countdown = 150
def setup():
    size(window_width, window_height)
    
    background(204, 0, 0)
       

def draw():
    global time_to_change
    global current_text_colour
    global current_background_colour
    global possible_colours
    global box_x
    global countdown
    global box_y
    global box_size
    if key == "1":
        time_to_change = 30
    elif key == "2":
        time_to_change = 60
    elif key == "3":
        time_to_change = 90
    elif key == "4":
        time_to_change = 120
    elif key == "5":
        time_to_change = 150
    elif key == "6":
        time_to_change = 180
    elif  key == "0":
        countdown = 150
    if (frame_count % time_to_change) == 0:
    
        text_rand = random.randint(0,len(possible_colours) - 1)
        background_rand = random.randint(0,len(possible_colours) - 1)
        if text_rand == background_rand:
            background_rand = (background_rand + 1) % len(possible_colours)

        current_text_colour = possible_colours[text_rand]
        current_background_colour = possible_colours[background_rand] 
  
    background(current_background_colour[0], current_background_colour[1], current_background_colour[2])

    fill( current_text_colour[0], current_text_colour[1], current_text_colour[2], 255)
    

    if countdown >= 0:
        letters = [zero, one, two,three]
        letter = letters[int(countdown/40)]
        countdown -= 1
        for y in range(0, font_size):
            for x in range(0, font_size):
                if letter[y][x]==1:
                    rect(box_x + (x * box_size),box_y + (y * box_size), box_size, box_size )

    


def key_pressed(event):
    
    pass


run(frame_rate=60)

