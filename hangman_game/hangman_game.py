#IMPORTS
from files.hangmanwordbank import HANGMANPICS
import random
from os import system


def correct_word(word_incomplete):
    """This methods loads the winner word from words.txt what is located in data folder

    Args:
        word_incomplete ([List]): [I use this list to give it a '-' symbol for every letter that winner word have,
        with purpose to show it in the screen when game begin]

    Returns:
        [str]: [This winner word is the word that I'm going to use on the match]
    """
    random_number = random.randint(1, 171)
    cont = 0

    with open("./files/words.txt", "r", encoding="utf-8") as f:
        
        file = [ data for data in f ]
        winner_word = file[random_number].removesuffix('\n')
        limit = len(winner_word)

        cont = 0

        while cont < limit:
            word_incomplete.append('-')
            cont += 1

        return winner_word

# Python program to convert a list to string

# Function to convert


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def compare_letter(letter_try, winner_word, word_incomplete, letter_tries, lives, hang):
    """This function is the main screen of the game, I use it for calculate how the game is going

    Args:
        letter_try ([str]): [It's the letter that user input]
        winner_word ([str]): [Represents the winner word that correct_word generate]
        word_incomplete ([List]): [I use this list to give it a '-' symbol for every letter that winner word have,
        with purpose to show it in the screen when game begin]
        letter_tries ([List]): [Save all the letters that user try in game]
        lives ([int]): [The lives of the player]
        hang ([List]): [Grafical design of the hangman]

    Returns:
        [type]: [description]
    """

    status = False
    correct = False
    for pos, char in enumerate(winner_word):
        if letter_try == char:
            correct = True 
            if any(letter in letter_try for letter in letter_tries) == False:
                word_incomplete[pos] = letter_try 
    if correct == False:
        lives -= 1 
        hang += 1              
    letter_tries.append(letter_try)
    if listToString(word_incomplete) == winner_word:
        status = True
    return status, lives, hang 


def run():
    """Here I use the compare_letter function, and decide the print's output of the game
    """
    word_incomplete = []
    winner_word = correct_word(word_incomplete)
    letter_tries = []
    attempt = False
    lives = 6
    hang = 0


    while attempt == False and lives > 0:
        system('cls')
        print(HANGMANPICS[hang])
        print('Guess the word! ' + 'You have ' + str(lives) + ' lives!')
        show_word = ' '.join([str(item) for item in word_incomplete])
        print(show_word.upper())
        print('\n')
        letter_try = input('Insert a letter: ')
        if letter_try.isalpha() and len(letter_try) == 1:
            attempt, lives, hang = compare_letter(letter_try, winner_word,
                                            word_incomplete, letter_tries,
                                            lives, hang)
        else:                    
            print("PLEASE, INTRODUCE ONE LETTER" + '\n')                    
    if attempt:
        print('You win! The word was ' + winner_word)
    if lives == 0:
        print(HANGMANPICS[hang])
        print('YOU LOSE!')


if __name__ == '__main__':
    run()
