import math
#This is my attempt at completing the Chapter One and Two Exercises.
print("This is Round Exercise:")
print('-'*100)
print(round(40.5))
print(round(41.5))
print(round(42.5))
print(round(43.5))
print(round(44.5))
print('-'*80)
print(round(43.4))
print(round(45.5))
print(round(43.6))
#after a few tries, I googled why round does that, and some nice folks at
# stackoverflow said round does that because round uses bankers rounding.
#bankers rounding tries to round to the nearest even integer.
#this means that half rounds to 0, One and a half rounds to two.
print('-'*80)
print('This is the second exercise' )
#make mistakes often and quickly, got it.
print(+2)
#putting a plus sign in front of a number doesn't seem to do anything.
print(2++2)
#putting two plus signs seems to add them normally
print(2+2)
print(3++3)
#yep, seems to just add them normally.
print("3 2")
#putting two numbers with no operator between them seems to cause an
# error, invalid syntax, with a suggestion that I may have forgotten a comma.
print(round(42.5))
print("round(42.5")
#removing one parenthetical causes an error, syntax error, with a suggestion
# that a parenthetical was never closed.
print("print_round425")
#removing all the parentheticals causes an error, name_error, name is not defined.
print('-'*80)
print("This is the third exercise")
#values and their types, make best guess then check with type.
print("I think that 765 is an integer")
print("I think that 2.718 is a integer")
print("I think that '2 pi' is an string")
print("I think that abs(-7) is a string")
print("I think that abs(-7.0) is a string")
print("I think that abs is an function")
print("I think that int is an string")
print("I think that type is an string")
print('-'*80)
print("Time to check!")
print(type(765))
print(type(2718))
print(type('2 pi'))
print(type(abs(-7)))
print(type(abs(-7.0)))
print(type (abs) )
print(type (int) )
print(type (type) )
#Type is a type, good to know. I was pretty sure that absolute value was a math
# function so while that wasn't in the chapter I was pretty sure that was the correct ish answer.
print('-'*80)
print("This is the fourth exercise")
#practicing writing arithmetic expressions
#how many seconds are there in 42 minutes 42 seconds?
print("step one, multiply fourty two by sixty")
print(42*60)
print("next, add twenty five twenty to fourty two")
print(2520+42)
print("There is Two thousand five hundred and sixty two seconds in 42 min & 42 sec.")
#how many miles in 10 kilometers? Hint: 1.61 km in a mile.
print("first we divide ten by one point five one")
print(10/1.61)
print("There are roughly Six point two one miles in 10 km.")
#If you run a 10-kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
print("step one, find pace for km per second")
print(10/2562)
print("the pace is roughly oh point zero zero three nine km per second.")
print("we can check by multiplying them both to make sure we get the same result, 10.")
print(0.0039032006245121*2562)
print("next we use our previously calculated distance of 10 km is 6.21 mi"
      " to calculate the pace of miles per second")
print(6.21/2562)
print("we can check if it is correct by multiplying them to make sure we get the same result, 6.21.")
print(0.002423887587822014*2562)
print("If we run a ten kilometer race in fourty two minutes and fourty two seconds, "
      "our average pace in seconds per mile is. 0.002423887587822014 per second")
#What is your average pace in minutes and seconds per mile?
print("step one, to find the pace in minutes and seconds per mile we can use"
      " our time and divide it by the miles.")
print(2562/6.21)
print("Next we divide 412.56038647342996 by 60.")
print(412.56038647342996/60)
print("next we multiply sixty by .876006441223833")
print(60*.876006441223833)
print("The average pace in minutes and seconds per mile is roughly six "
      "minutes and fifty two minutes per mile")
#What is your average speed in miles per hour?
print("to calculate the average speed in seconds per mile we can use the "
      "previously calculated minutes per mile.")
print("first we divide sixty by six point eighty seven.")
print(60/6.876006441223833)
print("the average speed in miles per hour is roughly eight point seven two miles per hour.")
print("Completed chapter one exercises.")
print('-'*80)
print('-'*80)
print("This is chapter two exercises")
#Trying new features for errors.
print("17 = n")
print( "Putting a seventeen equals n results in a syntax error, with a suggestion "
       "that we cannot assign to literal here, and maybe we meant ==." )
x=y=1
print("Using x equals y equals one seems to work, my guess is because both x and y "
      "can be allowed to equal one without issue..")
print(y+x)
#seems like it works fine.
print("n = 17;")
print("adding a semicolon to the end of a statement does not cause an error when "
      "run, but pycharm does suggest to remove the trailing semi-colon.")
m = 17.
print("adding a period to the end of a statement does not cause an error when run, and "
      "pycharm does not suggest anything is wrong.")
print("import maath")
print( "Putting a misspelled module results in a ModuleNotFoundError: No module named 'maath'" )
print("-"*120)
#Using the python interpreter as a calculator
#This is the start of part one, volume of a sphere.
#One, the volume of a sphere with radius r is four over three times Pi times r raised to the power of 3.
#What is the volume of a sphere with radius 5?
radius = 5
volume_of_a_sphere_with_radius_of_five = 4 / 3  * math.pi * radius ** 3
print(f'"The volume of a sphere with the radius of Five is four over three times Pi times r '
      f'raised to the power of 3 which equals: {volume_of_a_sphere_with_radius_of_five}"')\
#Comment added, indicating that radius is in centimeters and volume is in cubic centimeters.
#Let’s see if it is true for a specific value of x like fourty two.
Eks = 42
#This is the start of part two, trigonometry.
#Two, A rule of trigonometry says that for any value of x,
#open parenthetical cosine x close parenthetical raised to the power of two
#plus open parenthetical sine x close parenthetical raised to the power of two equals one.
print("The primary pythagorean identitiy of sine squared times x plus cosine squared times"
      " x should equal one ")
print("Using the given value for x of fourty two, we can see if The primary pythagorean "
      "identitiy of sine squared times fourty two plus cosine squared times fourty two "
      "actually equals to one ")
print( f'math.cos(Eks)**2 + math.sin(Eks)**2 = {math.cos(Eks)**2 + math.sin(Eks)**2} ')

#This is part three, the addition to pi
#Three, compute euler's number to the power of two in three ways.
print( f'Way one of computing eulers number raised to the power of two = {math.e ** 2} ' )
print( f'Way two of computing eulers number raised to the power of two = { math.pow(math.e, 2) } ' )
print( f'Way three of computing eulers number raised to the power of two = { math.exp(2) } ' )
print("The third way of computing eulers number raised to the power of two shows a more "
      "precise value in comparison to the first two ways. from my understanding the math.exp"
      " is likely using a more precise value for eulers number.  ")
print(math.e)
print(math.exp(1))
#goign a little searching on the internet I found the reason is, because the other two methods use a 16 digit long version of eulers
# number, but the third way uses the c library optimized algorithms to
# calculate floating point exponentiation
print("-"*120)
print("Chapter One and Two exercises completed!")