print("Hello World!")
print("This is the start of the Chapter Sixteen end of chapter Exercises!")
from copy import copy
import turtle

class Point:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def translated(self, dx=0, dy=0):
        point = copy(self)
        point.translate( dx, dy )
        return point

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)


class Line:
    def __init__(self, p1, p2, t:turtle.Turtle=None):
        self.t = t if t else turtle.Turtle()
        self.p1 = p1
        self.p2 = p2

    def jumpto(self):
        self.t.penup()
        self.t.goto(self.p1.x, self.p1.y)
        self.t.pendown()

    def draw(self):
        self.jumpto()
        self.t.goto(self.p2.x, self.p2.y)


    def midpoint(self) -> Point:

        return Point((self.p1.x + self.p2.x)/2, (self.p1.y + self.p2.y)/2 )

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'


    def __eq__(self, other):

        return (self.p1 == other.p1 and self.p2 == other.p2) or (self.p1 == other.p2 and self.p2 == other.p1)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["t"]
        return state


def main():

    screen = turtle.Screen()
    screen.bgcolor( "white" )

    screen.setup( width=600, height=600 )

    turt = turtle.Turtle()
    turt.clear()


    line1 = Line(Point(10,10), Point(100,100), t=turt)



    line1.draw()

    line2 = Line(Point(100,100), Point(10,10), t=turt)

    print(line1 == line2)

    line3 = Line(Point(101,100), Point(10,10), t=turt)
    # Compare for equivalence
    print(line1 == line3)


    line4 = Line(Point(3,0), Point(9, 0), t=turt)
    line5 = Line(Point(0,3), Point(0, 9), t=turt)
    line6 = Line(Point(3,3), Point(9, 9), t=turt)
    print(line4.midpoint())
    print(line5.midpoint())
    print(line6.midpoint())


    turtle.exitonclick()

p = Point(3,4)
print(p)
print(p.translated(10,10))


class Rectangle:


    def __init__(self, width, height, corner:Point, t:turtle.Turtle=None):
        self.t = t if t else turtle.Turtle()
        self.width = width
        self.height = height
        self.corner = corner

    def make_points(self) -> tuple[Point, Point, Point, Point]:
        p1 = self.corner
        p2 = p1.translated( self.width, 0 )
        p3 = p2.translated( 0, self.height )
        p4 = p3.translated( -self.width, 0 )
        return p1, p2, p3, p4

    def make_lines(self) -> tuple[Line, Line, Line, Line]:
        p1, p2, p3, p4 = self.make_points()
        return Line( p1, p2, t=self.t ), Line( p2, p3, t=self.t ), Line( p3, p4, t=self.t ), Line( p4, p1, t=self.t )

    def draw(self):
        lines = self.make_lines()
        for line in lines:
            line.draw()

    def grow(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

    def translate(self, dx, dy):
        self.corner.translate( dx, dy )


    def midpoint(self) -> Point:

        return Point(self.corner.x + self.width / 2, self.corner.y + self.height / 2)

    def make_cross_v2(self) -> tuple[Line, Line]:
        midpoints = []

        for line in self.make_lines():
            midpoints.append( line.midpoint() )

        p1, p2, p3, p4 = midpoints
        return Line( p1, p3, t=self.t ), Line( p2, p4, t=self.t )


    def make_cross(self) -> list[Line]:

        cross_lines = []
        lines = self.make_lines()
        mp1 = mp2 = 0
        for i, line in enumerate(lines):
            if i == 0:
                mp1 = line.midpoint()
            elif i == 1:
                mp2 = line.midpoint()
            elif i == 2:
                cross_lines.append(Line(mp1, line.midpoint(), t=self.t))
            elif i == 3:
                cross_lines.append(Line(mp2, line.midpoint(), t=self.t))
        return cross_lines

    def __str__(self):
        return f'Rectangle({self.width}, {self.height}, {self.corner})'

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["t"]
        return state


def main_2():

    screen = turtle.Screen()
    screen.bgcolor( "white" )

    screen.setup( width=600, height=600 )

    turt = turtle.Turtle()
    turt.speed(10)
    turt.clear()

    corner = Point( 20, 20 )
    rect1 = Rectangle( 100, 50, corner, t=turt)
    print( rect1 )
    rect1.draw()
    print(f"{rect1} midpoint: {rect1.midpoint()}")

    rect2 = Rectangle( 100, 50, corner, t=turt)
    print( f"Rect 2 before {rect2}" )

    from copy import deepcopy
    rect3 = deepcopy( rect2 )
    rect3.t = turt
    print( f"Rect 3 before {rect3}" )

    rect2.translate( 50, 30 )
    print( f"Rect 2 after translate {rect2}" )
    rect3.grow( 100, 60 )
    print( f"Rect 3 after grow {rect3}" )

    rect2.draw()
    rect3.draw()

    print(f"{rect1} midpoint: {rect1.midpoint()}")
    print(f"{rect2} midpoint: {rect2.midpoint()}")
    print(f"{rect3} midpoint: {rect3.midpoint()}")

    line1, line2 = rect3.make_cross()
    print(line1, line2)
    line1, line2 = rect3.make_cross_v2()
    print(line1, line2)

    line1.draw()
    line2.draw()


    turtle.exitonclick()

class Circle:

    def __init__(self, radius, center:Point, t:turtle.Turtle=None):
        self.t = t if t else turtle.Turtle()
        self.radius = radius
        self.center = center

    def draw(self):
        start_y = self.center.y - self.radius
        self.t.penup()
        self.t.goto(self.center.x, start_y)
        self.t.pendown()
        self.t.circle(self.radius)

    def __str__(self):
        return f'Circle({self.radius}, {self.center})'

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["t"]
        return state


def main_3():

    screen = turtle.Screen()
    screen.bgcolor( "white" )

    screen.setup( width=600, height=600 )

    turt = turtle.Turtle()
    turt.speed(5)
    turt.clear()


    circle1 = Circle(50, Point(-20, -20), t=turt)
    circle1.draw()


    turtle.exitonclick()


print("This is the end of the Chapter Sixteen end of chapter Exercises.")
