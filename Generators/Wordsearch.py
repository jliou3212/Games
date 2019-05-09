import random


# generates a 2d array filled with 0's
def empty_board(size):

    return [[0] * size for i in range(size)]


# generates list of random words from list of 10000~ english words
def random_words(amt):
    file_name = "english_words_common.txt"
    file = open(file_name, 'r')
    old_words = [line.rstrip() for line in file]
    new_words = []
    for i in range(amt):
        randnum = random.randrange(0, len(old_words)+1)
        new_words.append(old_words[randnum])
    return new_words


# inserts one word into the board
def insert_word(b1, w1):
    # selects starting position for word
    startx = random.randrange(0, len(b1))
    starty = random.randrange(0, len(b1))
    b1[startx][starty] = w1[0]

# TODO determine list of illegal movements through conditionals
    while True:
        if not len(w1) + startx > len(b1):
            if not startx - len(w1) < 0:
        if not len(w1) + starty > len(b1):
            if not starty - len(w1) < 0:

    randx = random.randrange(-1, 2)
    randy = random.randrange(-1, 2)
    return b1


# fills board with list of words
def fill_board(b1, l1):
    pass


# prints board in 2d array
def display_board(b1):
    for line in b1:
        print(line)


if __name__ == '__main__':
    board = empty_board(5)
    words = random_words(7)
    fill_board(board, words)
    board = insert_word(board, "test")
    display_board(board)

