import pyglet
import random
def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

# Create a window
window = pyglet.window.Window(width=810, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a sorted list with random numbers ensuring 11 is included
numbers = sorted(random.sample(range(1, 100), k=20) + [11])


# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = left + (right - left) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = left + (right - left) // 2
        if numbers[mid] == 11:
            found = True
        elif numbers[mid] < 11:
            left = mid + 1
        else:
            right = mid - 1
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
        if left <= i <= right and not search_complete:
            color = hex_to_rgb('#7BD3EA')  # color for the current search interval 
        elif i == mid and not search_complete:
            color = hex_to_rgb('#FFE569') # color for the middle element
        elif found and i == mid:
            color = hex_to_rgb('#FF90BB')  # color for the number that found 
        else:
            color = hex_to_rgb('#424769')  # color for the eliminated elements
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()
pyglet.clock.schedule_interval(lambda dt: binary_search(), 1)

pyglet.app.run() 