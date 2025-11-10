# The following is Turtle code that will draw a square and a triangle.
# The triangle function has an error, find it and fix it.
# You have 10 minutes to complete this task.

# NOTE: bug is angle in triangle should be 120, not 180

import turtle

def draw_square(L):
    """Draw a square with side length L"""
    for i in range(4):
        turtle.forward(L)
        turtle.right(90)

def draw_triangle(L):
    """Draw a triangle with side length L"""
    for i in range(3):
        turtle.forward(L)
        turtle.right(190)

# Draw a square with side length 100
L = 100
# draw_square(L)

# Draw a triangle with side length 100
T = 100
draw_triangle(T)

# Keep the window open
turtle.done()
