print('This is the start of the chapter twelve exercises')


import unicodedata

def get_punctuation(filename):
    punc_marks = {}
    with open(filename, encoding='utf-8') as fp:
        for line in fp:
            for char in line:
                category = unicodedata.category( char )
                if category.startswith( 'P' ):
                    punc_marks[char] = 1
    return ''.join(punc_marks)

def split_line(line):
    return line.replace('—', ' ').split()

def clean_word(word, punctuation):
    return word.strip(punctuation).lower()

def process_word_trigram(word, window, trigram_counter):
    window.append( word )
    if len(window) == 3:
        count_trigram(window, trigram_counter)
        window.pop(0)  # Shift the window by removing the first element.

def count_trigram(trigram, trigram_counter):
    key = tuple(trigram)
    trigram_counter[key] = trigram_counter.get(key, 0) + 1

def find_max(counter):
    v_max = 0
    max_key = None
    for k,v in counter.items():
        if v > v_max:
            v_max = v
            max_key = k
    return max_key, counter[max_key]

def find_max_v2(counter):
    max_key = sorted(counter, key=lambda key: counter[key])[-1]
    return max_key, counter[max_key]

def find_max_v3(counter):
    max_key =max(counter, key=lambda key: counter[key])
    return max_key, counter[max_key]

def extract_book_text(lines):
    in_book = False
    for line in lines:
        if line.startswith("*** START OF"):
            in_book = True
            continue
        if line.startswith("*** END OF"):
            break
        if in_book:
            yield line

def main():
    file_path = 'book/dr_jekyll_and_mr_hyde.txt'
    window = []
    trigram_counter = {}
    punctuation = ".,;:!?\"()[]{}"

    with open(file_path, 'r', encoding='utf-8') as fp:
        for line in extract_book_text(fp):
            #for word in line.split():
            for word in split_line(line):
                word = clean_word(word, punctuation)
                if not word:
                    continue
                process_word_trigram(word, window, trigram_counter)
    print(find_max(trigram_counter))

#remove THIS to use># main()





from pprint import pprint  # For pretty-printing my successor map

def add_trigram(trigram, successor_map):
    first, second, third = trigram
    key = (first, second)
    #successor_map.setdefault((first, second), set()).add(third)
    successor_map.setdefault((first, second), []).append(third)

def load_successor_map(file_path, window, successor_map):
    punctuation = get_punctuation(file_path)
    with open(file_path, 'r', encoding='utf-8') as fp:
        for line in fp:
            for word in line.split():
                word = clean_word(word, punctuation)
                process_word_trigram(word, window, successor_map)

def main_2():
    file_path = 'book/dr_jekyll_and_mr_hyde.txt'
    window = []
    successor_map = {}
    load_successor_map(file_path, window, successor_map)
    pprint(successor_map, indent=4)

#remove THIS to use># main_2()




from pprint import pprint

def process_word_trigram(word, window, successor_map):
    window.append(word)
    if len(window) == 3:
        add_trigram(window, successor_map)
        window.pop(0)

def add_trigram(trigram, successor_map):
    first, second, third = trigram
    key = (first, second)
    successor_map.setdefault(key, []).append(third)

def load_successor_map(file_path, window, successor_map):
    punctuation = get_punctuation(file_path)
    with open(file_path, 'r', encoding='utf-8') as fp:
        for line in extract_book_text(fp):
            for word in split_line(line):
                word = clean_word(word, punctuation)
                if not word:
                    continue
                process_word_trigram(word, window, successor_map)

def main_3():
    file_path = 'book/dr_jekyll_and_mr_hyde.txt'
    window = []
    successor_map = {}
    load_successor_map(file_path, window, successor_map)
    pprint(successor_map, indent=4)

#remove THIS to use># main_3()




from random import choice

def main_4():
    # file_path = 'files/half_a_bee.txt'
    file_path = 'files/dr_jekyll_and_mr_hyde.txt'
    window = []
    successor_map = {}
    punctuation = get_punctuation( file_path )
    load_successor_map(file_path, window, successor_map)
    successors = list(successor_map)
    bigram = choice(successors)

    line = ''
    for i in range(50):
        next_words = successor_map[bigram]
        word = choice(list(next_words))
        line += ' ' + word
        if len(line) >= 75:
            print(line)
            line = ''
        bigram = (bigram[1], word)


#remove THIS to use># main_4()