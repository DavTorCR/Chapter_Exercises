print("Hello World - Are you ready to draw? ")

"""This is the start of the chapter four exercises"""


import turtle
import math



def polyline(n, length, angle):  # This is really generalized and flexible now.
    """Draws line segments with the given length and angle between them.

    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degrees)
    """
    for i in range(n):
        my_turtle.forward(length)
        my_turtle.left(angle)

def polygon(n, length):
    angle = 360.0 / n
    # Now this is more generalized as it uses polyline, but still fixes the length and angle for regular polygons.
    polyline(n, length, angle)


def jump(my_turtle, x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()


# exercise 4.11.1

"""Write a function called rectangle with the given side lengths 80 * 40 """

def rectangle(b, h):
    """Takes a base and height and draws a rectangle using polyline.

    :param b: width of the rectangle, or its base
    :param h: height of the rectangle
    :return: None
    """
    for i in range(2):  # Since a rectangle is 2 symmetric bases and heights
        for s in (b, h):  # iterate: draw base, turn 90, draw height turn 90
            polyline(1, s, 90)


"""Write a function called rhombus with the given side lengths of 
50 and interior angle of 60 degrees """

def rhombus(base, interior_angle):
    """Draws a rhombus of varying length and angle.

    :param base: Length of side of rhombus. Rhombus have equal lengthened sides
    :param interior_angle: The first interior angle of a rhombus, the complementary angle will bie 180 minus this angle
    :return: None
    """
    for i in range(2):  # A rhombus is also symmetric like the rectangle, draw a pair of base angle parts.
        for angle in (interior_angle, 180 - interior_angle):  # draw base, turn small angle, draw base, turn sharp angle
            polyline(1, base, angle)



"""Write a function called parallelogram with parallel given side lengths and redraw
rectangle, rhombus """


def parallelogram(base, leg, interior_angle):
    """Draws a quadrilateral with parallel sides, a more generalized form of rhombus and rectangle.

    :param base: base of quadrilateral
    :param leg: side of quadrilateral
    :param interior_angle: first interior angle of quadrilateral
    :return: None
    """
    for i in range(2):  # Just like rhombus and rectangle before, there are 2 symmetric parts.
        for side, angle in ((base, interior_angle), (leg, 180 - interior_angle)):
            # Draw base and turn, then draw leg and turn complementary
            polyline(1, side, angle)

def rhombus_two(base, interior_angle):
    """Rhombus drawn with generalized parallelogram / quadrilateral function

    :param base: side of rhombus
    :param interior_angle: First interior angle of rhombus
    :return: None
    """
    parallelogram(base, base, interior_angle)

def rectangle_two(b, h):
    """Rectangle drawn with generalized parallelogram / quadrilateral function

    :param b: base of rectangle
    :param h: height of rectangle
    :return: None
    """
    parallelogram(base=b, leg=h, interior_angle=90)


""" Write a function called isosceles that can draw different shapes as shown in the textbook,
 a pentagon, a hexagon, and a heptagon """


def isosceles_triangle(leg, base_angle):
    base = 2 * leg * math.sin(math.radians(90 - base_angle))  # Length of the base of a triangle.
    angle = 180 - base_angle
    polyline(1, leg, angle)
    polyline(1, base, angle)
    polyline(1, leg, 2 * base_angle)

def draw_pie(n, leg):
    """Uses isosceles_triangle to draw the triangle parts of regular polygons.

    :param n: Number of sides of  polygon
    :param leg: Length of side of isosceles triangle forming polygon triangles.
    :return: None
    """
    base_angle = 90 - 180 / n  # The base angle of the isosceles triangle
    center_angle = 2 * base_angle  # The center angle of the triangle in the center of the polygon
    # print(f"B:{base_angle}\nC:{center_angle}\n")
    for i in range(n):  # Loop on the number of sides/triangles we need to create.
        isosceles_triangle(leg, base_angle)  # Draw a triangle
        my_turtle.left(180 - center_angle)   # Turn turtle to location for next triangle





""" Write a function that can draw different flowers as shown in the textbook,
 a pentagon, a hexagon, and a heptagon """


def arc(radius, angle):  # Similar to circle, but can do fractional circles.
    arc_length = 2 * math.pi * radius * angle / 360  # Here we calculate how much of the arc of a circle to draw.
    n = 30  # We fix the segments to 30 still, but this is 30 segments per arc, so smaller arcs will appear smoother.
    length = arc_length / n
    step_angle = angle / n  # Since we are covering a fraction of the arc of a circle, we need smaller angles too.
    polyline(n, length, step_angle)  # And now we approximate the arc with polyline.


def petal(radius, angle=90):
    return_angle = 180 - angle
    for i in range(2):
        arc( radius, angle )
        my_turtle.left( 180 - angle )


def flower(num_petals, radius, petal_angle=None):
    rotate_angle = 360 / num_petals
    petal_angle = rotate_angle if not petal_angle else petal_angle
    for p in range(num_petals):
        petal(radius, petal_angle)
        my_turtle.left(rotate_angle)

"""This is the function we are to use to draw a circle:"""
def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)


# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=1000, height=1000)

# Create a new turtle object, equivalent to Jupyter's make_turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape and color
my_turtle.shape( "turtle" )  # Other options: arrow, classic, square, triangle, and turtle
# Set the turtle's color
my_turtle.color( "White" )
"""many available turtle colors viewable at this website: https://cs111.wellesley.edu/reference/colors """


# Let's start Drawing with my Turtle.
my_turtle.speed(10)  # controls speed (from 1-10, slowest to faster | 0 fastest)

jump(my_turtle, -450, -450)

rectangle(80, 40)

jump(my_turtle, -450, -400)

rhombus(50, 60)

jump(my_turtle, -350, -300)

my_turtle.color( "cyan" )
parallelogram(200, 100, 60)

jump(my_turtle, -350, -300)

my_turtle.color( "salmon" )
rhombus_two(50, 60)

jump(my_turtle, -250, -250)

my_turtle.color( "green" )
rectangle_two(100, 50)
# Close the turtle graphics window when clicked

jump(my_turtle, -200, -200)

# isosceles_triangle(100, 40)
my_turtle.color( "yellowgreen" )
draw_pie(5, 50)

jump(my_turtle, -150, -150)

my_turtle.color( "red" )
draw_pie(6, 100)

jump(my_turtle, -100, -100)


my_turtle.color( "purple" )
draw_pie(7, 150)


jump(my_turtle, -50, -50)

my_turtle.color( "pink" )
draw_pie(8, 200)


jump(my_turtle, 0, 0)
my_turtle.color( "pink" )
flower(10, 90, 90)

jump(my_turtle, 300, 300)

flower(7, 90, 90)
jump(my_turtle, 300, 270)
draw_circle(my_turtle, 20)


turtle.exitonclick()


