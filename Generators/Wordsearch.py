import random


def empty_board(size):
    # generates a 2d array filled with 0's

    return [[0] * size for i in range(size)]


def random_words(amt):
    # generates list of random words from list of 10000~ english words
    file_name = "english_words_common.txt"
    file = open(file_name, 'r')
    old_words = [line.rstrip() for line in file]
    new_words = []
    for i in range(amt):
        randnum = random.randrange(0, len(old_words)+1)
        new_words.append(old_words[randnum])
    return new_words


def fill_board(b1, l1):
    # fills board with list of words
    pass

if __name__ == '__main__':
    board = empty_board(5)
    words = random_words(7)
    print(words)

