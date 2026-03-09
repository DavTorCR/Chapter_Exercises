print("Hello World.")
def lb():
    print("-"*40)

print("This is the Start of the Chapter Seven Exercises.")

lb()

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.

#    >>> uses_none('banana', 'xyz')
    True
#    >>> uses_none('apple', 'efg')
    False
#    >>> uses_none('thimbleberry', 'nop')
    True
#   >>> uses_none('sierra gooseberry', 'abc')
    False
    """
    word = word.lower()
    for l in forbidden.lower():
        if l in word:
            return False
    return True

# run_doctests(uses_none) # remove comment hash to run doctests (4)

#print(uses_none('banana', 'xyz'))
#print(uses_none('apple', 'efg'))
#print(uses_none('thimbleberry', 'nop'))
#print(uses_none('sierra gooseberry', 'abc'))

# referencing the Calflora Database ( https://www.calflora.org/ )
# Using Calfloras' "What grows here?" search tool, I found a new fruit to add to the doc test:
# Rubus parviflorus, the thimble berry.
# interestingly, the interactive map shows that there is two sightings of the thimble berry
# at Sequoia park, there is even a photo available for one of the sighting that really does look
# like the thimbleberry's flower.
#
# Sources :
# https://www.calflora.org/entry/occdetail.html?seq_num=in:12930888&taxon=Rubus+parviflorus
# https://en.wikipedia.org/wiki/Rubus_parviflorus
#
# I am thinking of heading over there and seeing if I can find it in person,
# as Califlora shows that thimbleberry's bloom period is March, April, May.
# I also found Ribes roezlii, the Sierra gooseberry, with the interactive map showing
# that there is a recent sighting that is also close to the harbor lanes bowling alley, the
# photo corresponding to the sighting also looks really nice.
#
# Sources :
# https://www.calflora.org/entry/occdetail.html?seq_num=mu24376&taxon=Ribes+roezlii
# https://en.wikipedia.org/wiki/Ribes_roezlii
#
# (the location is of a backyard, so I will NOT be trying to look for it.)
print("Added Two Doctests to uses none function, thimbleberry, nop | true and sierra gooseberry, abc | false.")

lb()

def uses_only(word, available):
    """Checks whether a word uses only the available letters.

#    >>> uses_only('banana', 'ban')
    True
#    >>> uses_only('apple', 'apl')
    False
#    >>> uses_only('kiwi', 'kiw')
    True
#    >>> uses_only('cantaloupe', 'can')
    False
    """
    available = available.lower()
    for l in word.lower():
        if l not in available:
            return False
    return True

# run_doctests(uses_only)# remove comment hash to run doctests (4 + 4)

#print(uses_only('banana', 'ban'))
#print(uses_only('apple', 'efg'))
#print(uses_only('kiwi', 'kiw'))
#print(uses_only('cantaloupe', 'can'))

# it took me a couple of re-reads to understand why my first few doctests weren't working.

print("Added Two Doctests to uses only function, kiwi, kiw | true and cantaloupe, can  | false.")

lb()

def uses_all(word, required):
    """Checks whether a word uses all required letters.

#    >>> uses_all('banana', 'ban')
    True
#    >>> uses_all('apple', 'api')
    False
#    >>> uses_all('grapefruit', 'gra')
    True
#    >>> uses_all('mamoncillo', 'xyz')
    False
    """
    required = required.lower()
    for l in word.lower():
        if l in required:
            required = required.replace(l, '')
        if len(required) == 0:
            return True
    return False

# run_doctests(uses_all) # remove comment hash to run doctests (4 + 4 + 4)

#print(uses_all('banana', 'ban'))
#print(uses_all('apple', 'api'))
#print(uses_all('grapefruit', 'gra'))
#print(uses_all('mamoncillo', 'xyz'))

# it took me a couple of re-reads to understand why my first few doctests weren't working.

print("Added Two Doctests to uses all function, grapefruit, gra | true and mamoncillo, xyz  | false.")

lb()

def check_word(word, available, required):
    """Check whether a word is acceptable.

#    >>> check_word('color', 'ACDLORT', 'R')
#    True
#    >>> check_word('ratatat', 'ACDLORT', 'R')
#   True
#   >>> check_word('rat', 'ACDLORT', 'R')
#   False
#   >>> check_word('told', 'ACDLORT', 'R')
#   False
#   >>> check_word('bee', 'ACDLORT', 'R')
#   False
    """
    if len(word) < 4: return False
    word = word.lower()
    if not required.lower() in word: return False
    return uses_only(word, available)


def word_score(word, available):
    """Compute the score for an acceptable word.

#   >>> word_score('card', 'ACDLORT')
#   1
#   >>> word_score('color', 'ACDLORT')
#   5
#   >>> word_score('cartload', 'ACDLORT')
#   15
    """
    score = len(word) if len(word) > 4 else 1
    if uses_all(word, available): score += 7
    return score

#run_doctests(check_word)
#run_doctests(word_score)

lb()

def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.

#    >>> uses_none('banana', 'xyz')
    True
#    >>> uses_none('apple', 'efg')
    False
#    >>> uses_none('', 'abc')
    True
    """
    return not uses_any( word, forbidden )

def uses_all(word, required):
    """Checks whether a word uses all required letters.

#    >>> uses_all('banana', 'ban')
    True
#    >>> uses_all('apple', 'api')
    False
#    >>> uses_all('pawpaw', 'paw')
    True
#    >>> uses_all('persimmon', 'xyz')
    False
    """
    # return uses_only(word, required) and len(set(word)) == len(required)
    return uses_only(required, word)

#run_doctests(uses_all)
#run_doctests(uses_none)

#print(uses_all('banana', 'ban'))
#print(uses_all('apple','api'))
#print(uses_all('pawpaw', 'paw'))
#print(uses_all('persimmon', 'xyz'))

# taking some time to find other fruits to use for the doctests, I found pawpaws, a fruit that
# looks like a green to brown berry that apparently tastes like banana and pineapple which grows
# around temperate areas that are native to the eastern North America.
# Source:
# https://en.wikipedia.org/wiki/Asimina_triloba

print("Added Two Doctests to uses all function, pawpaw, paw | true and persimmon, xyz  | false.")

print("End of Chapter Seven Exercises")
lb()