from Hangman.main import get_word, get_initial_positions, hide_word, check_guess, check_for_win


def play_hangman():
    word = get_word()
    lives = 5
    positions = get_initial_positions(len(word))
    print(hide_word(word, positions))


    while True:
        win = False
        next_letter = input()
        new_positions = check_guess(word, next_letter, positions)

        if new_positions == positions:
            print('No such letter or already guessed')
            print(f'Lives remaining: {lives - 1}')
            lives = lives - 1

            if lives == 0:
                print('You lose!')
                break

        elif check_for_win(new_positions):
            print('You win!')
            break

        else:
            print('Another letter guessed!')
            print(hide_word(word, new_positions))
            positions = new_positions


play_hangman()