from hangman_words import*
from hangman_body import*
import random
import string

def get_random_word():
    word = random.choice(words)
    return word

def print_guess(guess):
    list_guess = list(guess)
    guess = ' '.join(list_guess)
    print(f'Word: {guess}')

def guess_letter():
    letter = input('Guess letter: ')
    return letter

def get_letter_index_in_word(letter, word):
    '''
    Function returns a letter's indexes in word.
    '''

    indexes = list()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                indexes.append(i)
    return indexes

def change_guess_string(letter, guess, indexes):
    guess_list = list(guess)
    for i in indexes:
        guess_list[i] = letter
    
    return ''.join(guess_list)

def print_hangman(lifes):
    print(HANGMAN_BODY[len(HANGMAN_BODY) - lifes])

def main():
    alphabet = string.ascii_uppercase
    lifes = 7
    
    word = get_random_word()
    guess = '_' * len(word)
    print_hangman(lifes)
    print_guess(guess)

    while '_' in guess and lifes > 0:
        print("Letters: ", alphabet)
        letter = guess_letter()
        if letter.upper() in alphabet:
            alphabet = alphabet.replace(letter.upper(), " ")
            indexes = get_letter_index_in_word(letter, word)
            if len(indexes) == 0:
                lifes -= 1
            guess = change_guess_string(letter, guess, indexes)
            print_hangman(lifes)
            print_guess(guess)
        else:
            print("Wrong letter")

    if lifes > 0:
        print("Game over. You are a winner")
    else:
        print(f"Game over (word = {word})")

main()
