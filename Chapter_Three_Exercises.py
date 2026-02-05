print("-"*100)
print("Hello World!")
print("-"*100)
print("This is the start of Chapter Three Exercises")
print("-"*100)
print("3.11.2 exercise")
#Write a function named print_right that takes a string named text as a parameter and prints the string
# with enough leading spaces that the last letter of the string is in the 40th column of the display.


def print_right(word, spaces=40):
    print( f"{word:>{spaces}}" )

print_right("Sprite Zero")
print_right("Diet Dr.Pepper")
print_right("Red Bull")
#These have been the last three soda pops I have had in the last week, while I have been
# reading this week's chapter and completing this week's assignments.

print("-"*100)

#Write a function called triangle that takes a string and an integer and draws a pyramid with the
#given height, made up using copies of the string. Here’s an example of a pyramid with 5 levels
# , using the string 'L'.

print("3.11.3 exercise")

def triangle_inator(char,level):
    for i in range (level):
        print(char*(i+1))

triangle_inator('M', 61)

#The Pyramid of Menkaure is the shortest of the three main pyramids
# in the Giza Plateau which is 61 meters tall.

print("-"*100)
print("3.11.4 exercise")

# Write a function called rectangle that takes a string and two integers and draws a
# rectangle with the given width and height, made up using copies of the string.

def rectangle_inator(c, chols, rows):
    for j in range( rows ):
        print(c* chols)

rectangle_inator('||', 5 , 9)

# The length and height of the largest stone at stonehenge is roughly nine meters tall and five meters long

print("-"*100)

print("3.11.5 exercise")
#Write a function called bottle_verse that takes a number as a parameter and displays
# the verse that starts with the given number of bottles.


def bottle_verse(n):
    if n <= 0: return
    print(f"""{n} bottle{'' if n == 1 else 's'} of beer on the wall
{n} bottle{'' if n == 1 else 's'} of beer
take one down, pass it around
{n-1} bottle{'' if n-1 ==1 else 's'} of beer on the wall
    """)

def bottle_song(n):
    for verse in range (n, -1, -1):
        bottle_verse(verse)

bottle_song(99)

print("-"*100)
print("Chapter Three Exercises Completed")
print("-"*100)