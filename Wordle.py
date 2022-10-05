# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, WordleGWindow, N_COLS, N_ROWS

def wordle():
    # Choose Random word from list
    word = random.choice(FIVE_LETTER_WORDS).upper()

    # Test to be sure word is selected and saved
    #print(word)

    def enter_action(s):
        input = ""

        # Gets the row 
        r = gw.get_current_row()

        # Loop through to get input word
        c = 0
        while c < 5:
            input += gw.get_square_letter(r,c)
            c += 1

        # Check to see if the word is in the approved dictionary
        # Convert to lower case to compare in dictionary
        if input.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list.")
        else:
            gw.show_message("We slayed Milestone #2!")
        
        #Begin Coloring
        #if all 5 letters correct, all green and congrats message
        if input.upper() == word.upper():
            gw.show_message("You guessed the right word!")
            c = 0
            while c < 5:
                gw.set_square_color(r, c, CORRECT_COLOR) 
                c += 1
        else: #letter by letter
            c = 0
            wordletterlist = list(word)
            while c < 5:
                guessedletter = gw.get_square_letter(r, c)

                #if letter in the word and in correct spot
                if (guessedletter in word) and (guessedletter == wordletterlist[c]):
                    gw.set_square_color(r, c, CORRECT_COLOR)
                elif guessedletter in word: #if letter is in word, but not correct spot
                    gw.set_square_color(r, c, PRESENT_COLOR) 
                else: #if letter isn't in word
                    gw.set_square_color(r, c, MISSING_COLOR) 
                c += 1

        #Move active row down to next row
        r += 1
        gw.set_current_row(r)
        

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
