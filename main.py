import random
import re
import sys

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


class InvalidWordError(Exception):
    """Custom exception for invalid words."""
    pass


class InvalidWordsFile(Exception):
    """Custom exception for invalid words file."""
    pass


def read_words_file(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace and convert to lowercase
            word = line.strip().lower()

            # Ensure the word only contains characters a-z and is between 3 and 7 characters long
            if re.match("^[a-z]{3,7}$", word):
                words.append(word)
            else:
                raise InvalidWordError(f"Invalid word found: '{word}'")

    if not words:
        raise InvalidWordsFile("No valid words found in the file.")

    return words


def get_random_word(world_list):
    # This function returns a random string from the passed list of strings.
    word_index = random.randint(0, len(world_list) - 1)
    return world_list[word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):  # replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        guess = input('Guess a letter.').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def main():
    print('H A N G M A N')

    words = []

    try:
        words = read_words_file('words.txt')
        print(words)
    except InvalidWordError as e:
        print(e)
        sys.exit(1)

    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)
    game_is_done = False

    while True:
        display_board(missed_letters, correct_letters, secret_word)

        # Let the player type in a letter.
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

            # Check if the player has won
            found_all_letters = True
            for i in range(len(secret_word)):  # go through all the letters in the secret word
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print('Yes! The secret word is "' + secret_word + '"! You have won!')
                game_is_done = True
        else:
            missed_letters = missed_letters + guess

            # Check if player has guessed too many times and lost
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print('You have run out of guesses! After ' + str(len(missed_letters)) + ' missed guesses and ' + str(
                    len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
                game_is_done = True

        # Ask the player if they want to play again (but only if the game is done).
        if game_is_done:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                game_is_done = False
                secret_word = get_random_word(words)
            else:
                break


if __name__ == '__main__':
    main()
