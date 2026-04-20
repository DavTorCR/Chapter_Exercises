print("Hello world . . . ")
print("This is the start of the chapter thirteen exercises.")

import re
import os.path
import shelve
import hashlib

def replace_all(str_pattern, str_replace, file1, file2):
    with open(file1, 'r') as fp1, open(file2, 'w') as fp2:
        for line in fp1:
            line = re.sub(str_pattern, str_replace, line)
            fp2.write(line)

def main():
    replace_all(r'photos', 'images', 'photos/notes.txt', 'output/new_notes.txt')


def add_word(my_str, anagram_shelf: shelve.Shelf):
    word, key = get_word_and_key(my_str)
    if key in anagram_shelf:
        if word not in anagram_shelf[key]:  # Can't treat shelf like a dictionary because it needs to be synced to fs.
            anagram_list = anagram_shelf[key]
            anagram_list.append(word)
            anagram_shelf[key] = anagram_list
    else:
        anagram_shelf[key] = [word]
    anagram_shelf.sync()  # This is likely redundant, but whatever.
    return anagram_shelf  # No real need to return this, but whatever.

def prepare(word):
    return word.strip().lower()

def get_word_and_key(word):
    word = prepare(word)
    return word, ''.join( sorted( word ) )

def load_anagram_map(db_file='files/anagram_map.db'):
    if not os.path.exists(db_file):
        word_list_to_anagram_map(db_file=db_file[:-3])  # This ensures it is loaded first, and removes .db extension.

    return shelve.open(db_file[:-3], 'c')

def shelf_to_dict(db_file):
    my_dict = {}
    with shelve.open(db_file) as db:
        for key in db:
            my_dict[key] = db[key]
    return my_dict

def dict_to_shelf(my_dict: dict, db_file):
    with shelve.open( db_file, 'c' ) as db:
        for key, value in my_dict.items():
            db[key] = value

def word_list_to_anagram_map(word_list='files/words.txt', db_file='files/anagram_map'):
    anagram_map = {}
    with open(word_list, 'r') as fp:
        for word in fp:
            word, key = get_word_and_key(word)
            anagram_map.setdefault(key, []).append(word)
    dict_to_shelf(anagram_map, db_file)

def main_2():
    db = load_anagram_map()
    print(db.get('eorrtv'))
    db = add_word("Trevor", db)
    db.close()  # Force the write back of the word!

    db = load_anagram_map()
    print(db.get('eorrtv'))


def same_contents(path1, path2):
    data1 = open(path1, 'rb').read()
    data2 = open(path2, 'rb').read()
    return data1 == data2

def walk_images(directory, extensions, db, max_depth=-1):
    for root, dirs, files in os.walk(directory, topdown=True):
        if max_depth != -1:  # We only care about depth update if the parameter is set.
            depth = root.count(os.sep) - directory.count(os.sep)
            if depth >= max_depth:
                del dirs[:]

        for file in files:
            file = os.path.join(root, file)
            if is_image(file, extensions):
                add_path(file, db)

def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest

def add_path(file_path: str, db: shelve.Shelf):
    key = md5_digest(file_path)
    if key in db:
        if file_path not in db[key]:
            path_list = db[key]
            path_list.append(file_path)
            db[key] = path_list
    else:
        db[key] = [file_path]
    db.sync()  # This is likely redundant, but whatever.
    return db  # No real need to return this, but whatever.


def is_image(file_path: str, extensions: list):
    if not os.path.isfile(file_path): return False

    base_name, extension = os.path.splitext(file_path)
    if extension in extensions:
        return True
    return False

def main_3():
    extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.tiff']
    # print(is_image('photos/notes.txt', extensions))
    # print(is_image('photos/feb-2023/photo1.jpg', extensions))
    db = shelve.open( 'output/digests', 'n' )
    walk_images('photos', extensions, db)

    for digest, paths in db.items():
        if len( paths ) > 1:
            print( paths )
            print("Are they the same?", same_contents(*paths))


print("This is the end of the chapter thirteen exercises.")
