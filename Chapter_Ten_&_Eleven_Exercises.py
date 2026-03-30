print("Hello World.")
print("This is the start of the Chapter Ten Exercises.")

def value_counts_concise(word):
    counter = {}
    for l in word:
        counter[l] = counter.get(l, 0) + 1
    return counter
"""
    Checks what letters a word uses, and outputs results as a dictionary with number of times and letter used.

    >>>value_counts_concise('brontosaurus')
    {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

    >>>value_counts_concise('tyrannosaurus')
    {'t': 1, 'y': 1, 'r': 2, 'a': 2, 'n': 2, 'o': 1, 's': 2, 'u': 2}
"""

# a long word that has no letter repeated is called a first order isogram.
# Source:
# https://www.thoughtco.com/isogram-word-play-term-1691199

def has_duplicates_efficient(word):
    return len(set(word)) < len(word)

def has_duplicates_comprehension(word):
    return any(v > 1 for v in dict.values(value_counts_concise( word )))

def has_duplicates(word):
    counter = value_counts_concise(word)
    for k,v in counter.items():
        if v > 1:
            return True
    return False


"""
    Checks if word uses duplicate letters and outputs true if there are duplicates, or false if not.

    >>>has_duplicates('programming')
    True
    >>>has_duplicates('unpredictably')
    False

    >>>has_duplicates_efficient('programming')
    True
    >>>has_duplicates_efficient('unpredictably')
    False

    >>>has_duplicates_efficient('programming')
    True
    >>>has_duplicates_comprehension('unpredictably')
    False
"""

def find_repeats_v1(counter):
    repeats = []
    for k,v in counter.items():
        if v > 1:
            repeats.append(k)
    return repeats

def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    return [k for k,v in counter.items() if v > 1]

def add_counters_v1(counter1, counter2):
    result = dict(counter1)
    for k, v in counter2.items():
        result[k] = result.get(k, 0) + v
    return result

def add_counters(counter1, counter2):
    return {k: counter1.get(k, 0) + counter2.get(k, 0)
            for k in set(counter1.keys()).union(set(counter2.keys()))}

def load_word_list(file_path):
    word_list = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word_list[word.strip().lower()] = True
    return word_list

def is_interlocking(word, word_list=None):
    if word_list is None:
        word_list = {}
    word = word.lower()
    intword1 = word[0::2]
    intword2 = word[1::2]
    return intword1 in word_list and intword2 in word_list



print("This is the end of the Chapter Ten Exercises.")


print("This is the start of the Chapter Eleven Exercises.")

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range( len( letters ) )
letter_map = dict( zip( letters, numbers ) )

def shift_word(word, shift):
    ciphtertext = ''
    for l in word:
        l_index = (letter_map[l] + shift) % len(letters)
        ciphtertext += letters[l_index]
    return ciphtertext

def count_value(word):
    counter = {}
    for l in word:
        counter[l] = counter.get(l, 0) + 1
    return counter

def key_func(item):
    return item[1]

def most_frequent_letters(word):
    counter = count_value(word)
    # return dict( sorted( counter.items(), key=lambda item: item[1], reverse=True ) )
    return dict( sorted( counter.items(), key=key_func, reverse=True ) )


import json
from os.path import exists


def get_key(word):
    return ''.join(sorted(word.strip()))


def save_sorted_dict(word_dict, file_path):
    with open(file_path, 'w') as wd_file:
        json.dump(word_dict, wd_file, indent=True)


def load_sorted_dict(file_path):
    word_dict = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            key = get_key( word )
            key_list = word_dict.get( key, [] )
            key_list.append( word.strip() )
            word_dict[key] = key_list
    return word_dict

def load_word_dict(file_path, words_path='files/words.txt'):
    word_dict = {}
    if not exists(file_path):
        word_dict = load_sorted_dict(words_path)
        save_sorted_dict(word_dict, file_path)
    else:
        with open(file_path, 'r') as wd_file:
            word_dict = json.load(wd_file)
    return word_dict


def find_anagrams(word_list, word_dict):
    for word in word_list:
        key = get_key(word)
        if len(word_dict[key]) > 1:
            print(f'{word_dict[key]}')

def word_distance(word1, word2):
    return sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)

def word_distance_indexes(word1, word2):
    return [i for i, pair in enumerate(zip(word1, word2)) if pair[0] != pair[1]]


print("This is the end of the Chapter Eleven Exercises.")