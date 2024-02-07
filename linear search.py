import pyglet
import random

def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

# Create a window
window = pyglet.window.Window(width=850, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a list with random numbers ensuring 11 is included
numbers = random.sample(range(1, 100), 20) + [11]
random.shuffle(numbers)

# Variables to control the animation and search
current_index = 0
found_index = -1
search_complete = False

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 11:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True



@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # Draw the box
        if i == current_index and not search_complete:
            color = hex_to_rgb('#FFE569') #yellow
        elif i == found_index:
            color = hex_to_rgb('#FF90BB')  #pink
        else:
            color = hex_to_rgb('#7BD3EA') #blue
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)

pyglet.app.run()