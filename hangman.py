from hangman_words import*
from hangman_body import*
import random
import string

def get_random_word():
    word = random.choice(words)
    print(word)
    return word

def print_guess(list_guess):
    guess = ' '.join(list_guess)
    print(f'Word: {guess}')

def guess_letter(list_guess, word, alphabet):
    result = False
    letter = input('Guess letter: ')
    print(alphabet)
    alphabet = alphabet.replace(letter.upper(), ' ')
    print(alphabet)
    if letter in word:
        result = True
        for i in range(len(word)):
            if word[i] == letter:
                list_guess[i] = letter
    print_guess(list_guess)
    return result

def get_letter_index_in_word(letter, word):
    '''
    Function returns index of letter in word. 
    If letter doesn't exist in word fuunction returns False.
    '''
    pass

def print_hangman(lifes):
    print(HANGMAN_BODY[len(HANGMAN_BODY) - 1 - lifes])



def main():
    alphabet = string.ascii_uppercase
    
    word = get_random_word()
    guess = '_' * len(word)
    list_guess = list(guess)
    print_guess(list_guess)

    lifes = 7
    while '_' in list_guess and lifes > 0:
        print(f'Available letters: {alphabet}')
        if guess_letter(list_guess, word, alphabet) == False:
            lifes -= 1
            print('lifes', lifes)
            print_hangman(lifes)
    print("GAME OVER")

main()
