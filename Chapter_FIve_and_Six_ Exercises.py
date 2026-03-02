print('Hello world!')
print('this is the start of assignment end of chapter exercises five and six.')

#this is the time exercise

from time import time


now = time()

#Use integer division and the modulus operator to compute the number of days since
#January 1, 1970 and the current time of day in hours, minutes, and seconds.


days_since = now / 86400

print(f"It has been {days_since} days since the start of epoch time.")


import time

the_date = time.asctime()
print(f"Today's date is, {the_date}")

from time import mktime

def num_days(epoch_seconds):
    return int(epoch_seconds // 86400)  # 60s * 60m * 24h

def num_hours(epoch_seconds):
    return int(epoch_seconds // 3600)  # 60s * 60m

def num_minutes(epoch_seconds):
    return int(epoch_seconds // 60)  # 60m

def current_time_of_day_naive(epoch_seconds):
    return f"{ (num_hours(epoch_seconds)% 24):02d}:{(num_minutes(epoch_seconds)%60):02d}:{int(epoch_seconds % 60):02d}"

def current_time_of_day(epoch_seconds):
    # 3600 = 60m * 60s and we get hours since epoch, only minutes remain
    hrs_since_epoch, minutes = divmod(epoch_seconds, 3600)
    minutes, seconds = divmod(minutes, 60)  # Now we can get the whole minutes and the remaining seconds.
    # Now we can return the formated current time.
    # Since hours is since epoch, we need the modulus of 24hrs
    return f"{int(hrs_since_epoch % 24):02d}:{int(minutes):02d}:{int(seconds):02d}"


time_tuple = (2024, 9, 24, 10, 29, 65, 0, 0, 0)
now = mktime(time_tuple)
#now = time()
print(f"It has been {num_days(now)} days since the Unix epoch!")
print(f"Current epoch time {now} is: {current_time_of_day_naive(now)} GMT")
print(f"Current epoch time {now} is: {current_time_of_day(now)} GMT")


#excercise 2, triangle possible checker.
# Write a function named is_triangle that takes three integers as arguments, and that prints
# either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks
# with the given lengths.

def is_triangle_possible(s1, s2, s3):
    if s1 > s2 + s3:
        print("No")
    elif s2 > s1 + s3:
        print("No")
    elif s3 > s1 + s2:
        print("No")
    else:
        print("Yes")

def is_triangle(s1, s2, s3):
    print("No") if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2 else print("Yes")

is_triangle_possible(4, 5, 6)
is_triangle_possible(1, 2, 3)
is_triangle_possible(6, 2, 3)
is_triangle_possible(1, 1, 12)
is_triangle_possible(3, 4, 5)

print("~*"*45)

is_triangle(8, 4, 2)
is_triangle(6, 7, 6)
is_triangle(9, 1, 4)
is_triangle(9, 2, 7)
is_triangle(17, 7, 9)
is_triangle(1, 2, 3)
is_triangle(7, 7, 7)
print("~*"*45)
# exercise three, draw stack diagram of the program

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

print(f"Using python tutor, it appears that the textbook provided program recursively operates "
      f"upon 3 and 0, subtracting one from n (which starts at 3), and adding n to s "
      f"(which starts at 0) until n is 0, then ends with printing out the total of s "
      f"(which is 6). ")

print("~*"*45)

# exercise four, what the turtle doing?
# Read the following function and see if you can figure out what it does.
# Then run it and see if you got it right.
# Adjust the values of length, angle and factor and see what effect they have on the result.
# If you are not sure you understand how it works, try asking a virtual assistant.

"""
def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)

"""


print("-"*45)
print("OK, looking at the textbook provided program, it begins by importing instructions for "
      "changing directions, the next thing it does is define a function named draw that has one"
      "parameter, length, within the textblock it defines angle equals fifty and "
      "factor equals zero point six"
      "then it stipulates that if the parameter length is greater than 5, it instructs turtle"
      " to moves forward by the provided length, moves left by angle (50), "
      "draws using the value of factor (0.6) multiplied by length, then instructs turtle to move"
      " right by two multiplied by angle (50), then draws using the value of factor "
      "(50) multiplied by length, then instructs turtle to move left by angle (50),"
      "then it instructs turtle to move back by the provided length. "
      "it looks like turtle ")





# V remove triple quotes to use turtle

"""



import turtle

def draw(t:turtle, length):
    angle = 50
    factor = 0.6

    if length > 5:
        t.forward( length )
        t.left( angle )
        draw(t, factor * length )
        t.right( 2 * angle )
        draw(t, factor * length )
        t.left( angle )
        t.back( length )

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=500, height=500)

# Create a new turtle object, equivalent to Jupyter's make_turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape and color
my_turtle.shape( "turtle" )  # Other options: arrow, classic, square, triangle, and turtle
my_turtle.color( "green" )

# Draw with a turtle.
my_turtle.speed(0)

draw(my_turtle, 20)

# Close the turtle graphics window when clicked
turtle.exitonclick()


"""# < remove this to use turtle





print("~*"*45)
print("So, after running program, the textbook provided program appears to;"
      "if given a large length greater than 5, it draws a branching family tree looking image."
      "if given a length smaller than 5, it appears to draw nothing.")

print("~*"*45)

# exercise five, what are koch curves?

print("""Koch curves are one of the earliest fractals to have been described,
it is important because it shows how complex structures can arise from simple instructions.  """)

# V remove triple quotes to use turtle
""" 
import turtle

def snowflake(t:turtle, degree=60):
    n = 360 // degree
    for _ in range(n):
        koch( my_turtle, 120 )
        my_turtle.right( degree )


def koch(t:turtle, x):
    if x < 5:
        t.forward(x)
    else:
        koch(t, x/3)
        t.left(60)
        koch(t, x/3)
        t.right(120)
        koch(t, x/3)
        t.left(60)
        koch(t, x/3)

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=500, height=500)

# Create a new turtle object, equivalent to Jupyter's make_turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape and color
my_turtle.shape( "circle" )  # Other options: arrow, classic, square, triangle, and turtle
my_turtle.color( "green" )

# Draw with a turtle.
my_turtle.speed(10)  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).
# Let's do the snowflake
# koch(my_turtle, 120)
snowflake(my_turtle, 60)

# Close the turtle graphics window when clicked
turtle.exitonclick()


"""# < remove this to use turtle

print("~*"*45)

# exercise six, Sierpiński triangle.

# I asked llm for code to make a Sierpiński triangle
# V remove triple quotes to use turtle
"""
import turtle

def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def sierpinski(points, depth, t):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw_triangle(points, colormap[depth], t)

    if depth > 0:
        sierpinski([points[0],
                    midpoint(points[0], points[1]),
                    midpoint(points[0], points[2])],
                   depth - 1, t)

        sierpinski([points[1],
                    midpoint(points[0], points[1]),
                    midpoint(points[1], points[2])],
                   depth - 1, t)

        sierpinski([points[2],
                    midpoint(points[2], points[1]),
                    midpoint(points[0], points[2])],
                   depth - 1, t)

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()

points = [[-200, -100], [0, 200], [200, -100]]
sierpinski(points, 5, t)

screen.exitonclick()

"""# < remove this to use turtle

print("~*"*45)
print("the code made a nice looking Sierpiński triangle with different colors for the different parts of the triangles.")

print("End of Chapter Five Exercises.")

print("~*"*45)





