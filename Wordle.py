# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from audioop import mul
import random
from timeit import repeat
from typing import Counter

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

        # Right letters dictionary
        correctGuess = {}
        # Not in Word dictionary
        notIncluded = {}
        #In word but wrong spot dictionary
        yellow = {}
        # Repeat list to figure out what colors repeated letters should be
        repeat = []

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
            #gw.show_message("We slayed Milestone #2!")
        
            #Begin Coloring
            #if all 5 letters correct, all green and congrats message
            if input.upper() == word.upper():
                gw.show_message("You guessed the right word!")
                c = 0
                while c < 5:
                    gw.set_square_color(r, c, CORRECT_COLOR) 
                    c += 1

            # Else if word isn't right
            else: #letter by letter
                c = 0
                wordletterlist = list(word)

                while c < 5:
                    guessedletter = gw.get_square_letter(r, c)
                    # Establish what letters are correct and what aren't in the word
                    if (guessedletter in word) and (guessedletter == wordletterlist[c]):
                        # Add those indexes to the dictonary if green
                        correctGuess[c] = guessedletter
                    elif guessedletter not in word:
                        # Add those indexes to gray list
                        notIncluded[c] = guessedletter

                    c +=1

                x = 0
                while x < 5:
                    # Now get what letters aren't correct or not in the word
                    guessedletter = gw.get_square_letter(r, x)
                    if (x not in correctGuess) and (x not in notIncluded):
                    # does the letter appear multiple times in the guessed word?
                        if input.count(guessedletter) > 1: # Yes
                            # Create a list of all indicies for a repeated letter
                            t = 0
                            while t < 5:
                                if input[t] == guessedletter and (t not in correctGuess) and (t not in notIncluded): # and (input[t] not in yellow.values()):
                                    repeat.append(t)
                                t += 1

                            # counts up how many correct guesses of each letter
                            cor = Counter(correctGuess.values())

                            y = 0
                            mult = 0
                            # set necessary repeats to yellow and unnecessary ones to grey
                            while y < len(repeat):
                                if cor[guessedletter] + mult < word.count(guessedletter):
                                    yellow[repeat[y]] = guessedletter
                                    mult +=1
                                else:
                                    notIncluded[repeat[y]] = guessedletter
                                y +=1
                    x +=1

                # Output correct colors
                f = 0
                while f < 5:
                    if f in correctGuess:
                        gw.set_square_color(r, f, CORRECT_COLOR)
                    
                    elif f in yellow:
                        gw.set_square_color(r, f, PRESENT_COLOR) 
                    
                    else:
                        gw.set_square_color(r, f, MISSING_COLOR) 
                    f +=1

            #Move active row down to next row
            if r < 5:
                r += 1
                gw.set_current_row(r)
            else:
                gw.show_message("The word was " + word + ". Better luck next time!")
        # Right letters dictionary
        correctGuess = {}
        # Not in Word dictionary
        notIncluded = {}
        #In word but wrong spot dictionary
        yellow = {}
        # # Repeat dictionary
        # repeat = {}
        repeat = []
        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Milestone 1
    # # Print the random word in the five boxes across the first row of the window
    # # Initialize column to start at the far left
    # c = 0
    # # Iterate through every letter in the word
    # for l in word:
    #     # Set the letter in each spot
    #     gw.set_square_letter(0, c, l)
    #     # Output the letter in each spot
    #     gw.get_square_letter(0,c)
    #     # Move one column over for next iteration
    #     c += 1

# Startup code

if __name__ == "__main__":
    wordle()
