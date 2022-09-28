# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    # Choose Random word from list
    word = random.choice(FIVE_LETTER_WORDS)

    # Test to be sure word is selected and saved
    print(word)

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Print the random word in the five boxes across the first row of the window
    # Initialize column to start at the far left
    c = 0
    # Iterate through every letter in the word
    for l in word:
        # Set the letter in each spot
        gw.set_square_letter(0, c, l)
        # Output the letter in each spot
        gw.get_square_letter(0,c)
        # Move one column over for next iteration
        c += 1

# Startup code

if __name__ == "__main__":
    wordle()
