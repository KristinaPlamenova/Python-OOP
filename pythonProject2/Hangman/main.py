def get_word():
    word = input("Enter the secret word: ").lower()

    return word

def get_initial_positions(length):
    return [True, *([False] * (length - 2)), True]


def check_guess(word, letter, positions):
    new_positions = positions.copy()
    letter = letter.lower()
    for i in range(len(word)):
        if word[i] == letter:
            new_positions[i] = True

    return new_positions

def hide_word(word, positions):
    hidden = ''
    for index, letter in enumerate(word):
        if positions[index]:
            hidden += letter
        else:
            hidden += '-'

    return hidden



def check_for_win(position):
    for i in position:
        if i == False:
            return False
    return True








