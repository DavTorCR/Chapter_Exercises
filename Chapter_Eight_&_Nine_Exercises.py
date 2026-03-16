print("Hello World.")

print("-"*90)

print("This is the start of the end of Chapter Eight Exercises.")

print("-"*90)

def head(in_file, num_lines, out_file=None):
    lines = []
    with open(in_file, 'r') as file:
        for _ in range(num_lines):
            lines.append(file.readline())
    if out_file:
        with open(out_file, 'w') as file:
            file.writelines(''.join(lines))
    else:
        print(''.join(lines))

head('scratch_pad.py', 5, "outputs.txt") # switch file extension to do y py to write to the correct file
head('scratch_pad.py', 5)

print("-"*90)

def check_word(five_letter_word):
    five_letter_word = five_letter_word.upper()
    if 'E' not in five_letter_word:
        return False
    # Matches any world that has an E at the 3rd or 5th character or contains any of the letters SPADCLRK
    # \b is a word boundary, \w matches any character, ?: is a non-capturing group, {N} represents the
    # number of times a pattern occurs.
    pattern = r'\b(?:\w{2}E\w+|\w{4}E\w*|\w*[SPADCLRK]\w*)\b'
    return False if re.match(pattern, five_letter_word, re.IGNORECASE) else True

def run():
    print( check_word( 'BELLE' ) )
    print( check_word( 'JIVES' ) )
    print( check_word( 'HELLO' ) )
    print( check_word( 'ENJOY' ) )

def main():
    count = 0
    with open( 'scratch_pad.py', 'r' ) as file:
        for word in file:
            word = word.strip()
            if len( word ) == 5 and check_word( word ):
                print( word )
                count += 1

    print( f"A total of {count} words could still match." )

print("-"*90)

def check_word_two(five_letter_word):
    five_letter_word = five_letter_word.upper()
    if 'M' != five_letter_word[-1] or 'E' not in five_letter_word:
        return False
    # Matches any world that has an E at the 3rd or 5th character or contains any of the letters SPADCLRK
    # \b is a word boundary, \w matches any character, ?: is a non-capturing group, {N} represents the
    # number of times a pattern occurs.
    pattern = r'\b(?:\w{2}E\w+|\w{3}E\w+|\w{4}E\w*|\w*[SPADCLRK]\w*)\b'
    return False if re.match(pattern, five_letter_word, re.IGNORECASE) else True

def runi():
    print( check_word( 'BELLE' ) )
    print( check_word( 'JIVES' ) )
    print( check_word( 'HELLO' ) )
    print( check_word( 'ENJOY' ) )


def maini():
    count = 0
    with open( 'scratch_pad.py', 'r' ) as file:
        for word in file:
            word = word.strip()
            if len( word ) == 5 and check_word( word ):
                print( word )
                count += 1

    print( f"A total of {count} words could still match." )

print("-"*90)

import re

def check_pale(sentence):
   pattern = r'.*(pale\w*|pallor).*'
   return True if re.match(pattern, sentence) else False

def mainer():
    with open('cristo.py', 'r') as file:
        count = 0
        for line in file:
            if check_pale(line.strip()):
                print(line)
                count += 1

    print(f"Lines with some form of pale: {count}")

print("-"*90)

print("This is the end of Chapter Eight Exercises.")

print("-"*90)

print("This is the start of the end of Chapter Nine Exercises.")

print("-"*90)

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    return sorted(word1) == sorted(word2)

def run():
    print(is_anagram('tame', 'fame'))
    print(is_anagram('tops', 'stop'))

def main():
    count = 0
    with open('files/words.txt', 'r') as file:
        for word in file:
            word = word.strip().lower()
            if is_anagram(word, 'takes'):
                count += 1
                print(word)
    print(f'Found {count} anagrams for takes')

if __name__ == '__main__':
    # run()
    main()