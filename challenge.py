# [x] Greet the user welcoming them to the game
# [x] The program randomly selects a word from a list of 10 words with different lengths, you as the developer choose the words.
# [x] The program indicates to the user how many letters are in the word
# [x] The user is asked to guess a letter
# [x] If the letter is in the word, the letter is displayed in the correct position of the word with all previously guessed correct letters
# [x] If the letter is not in the word, display the letter indicating it is not in the word with all previously guessed letters that are not in the word
# [x] The program displays how many guesses have been made, with how many correct and incorrect guesses.
# [x] The program continues to ask the user for guesses until all the letters in the word are guessed correctly.
# [x] When all letters of the word are guessed correctly,
#   [x] a. the program tells the user they have correctly guessed the word
#   [x] b. and indicates the number of guesses it took
# [x] The program then asks the user if they would like to try again or quit
#   [x] a. If the user indicates they want to continue, the program chooses a different word randomly and the play continues
#   [x] b. If the user indicates they want to quit, the program thanks them for playing and quits.
# [x] You can choose to use a terminal interface or a web interface

# --- FLOW ---
# 1. Startup / Restart
#     - Greet user
#     - Pick word
#     - Indicate Letter quantity
# 2. Gameplay
#     - Guess letter
#     - Display correct & incorrect letter guesses
#     - Display number of correct & incorrect guess (maybe with picture)
#     - Continue until all letters are correctly guessed
# 3. Endgame
#     - Tell user that they found the word
#     - Tell user how many guesses they made
#     - Askes user if they'd like to try again or quit

# What's the best way to store word and guess data? We could use global variables.
# That should be ok for the number of guesses, but we will want to be able to 
# do lots of things like checking and printing the current letters in the word, so
# I'll probably use a Word class to represent the complete word and the incomplete 
# word and use methods to check guesses against the word and print out the incomplete
# word.

import random

num_correct_guesses = 0
num_incorrect_guesses = 0

current_word = None

guess_chars = []

class Word():

    def __init__(self, complete_word):

        self.complete = complete_word.lower()
        self.partial = ""

        for i in range(len(complete_word)):
            self.partial += "_"
    
    def __str__(self):
        string = "\n\n"

        for char in self.partial:
            string += char + " "

        return string.upper()
    
    def CheckGuess(self, guess_char):

        found_match = False

        new_partial = ""

        for index in range(len(self.complete)):

            matches_char = self.complete[index] == guess_char
            already_found = self.partial[index] != "_"

            if matches_char:
                found_match = True

            if matches_char or already_found:

                new_partial += self.complete[index]
            
            else:
                new_partial += "_"
        
        self.partial = new_partial
        
        return found_match
    
    def CheckCompleteness(self):

        word_complete = self.complete == self.partial

        return word_complete                  


def GameLoop(greeting_message):

    print(greeting_message)

    InitializeGame()
    PlayGame()
    

def InitializeGame():

    ResetGuesses()
    SelectWord()

def SelectWord():

    word_list = ["donut", "pizza", "anaconda", "supercalifragilisticexpialidocious",
                 "office", "information", "technology", "foobar", "moroni", "cowboy"]
    
    global current_word

    new_word_string = random.choice(word_list)

    current_word = Word(new_word_string)

def ResetGuesses():

    global num_correct_guesses
    global num_incorrect_guesses
    global guess_chars

    num_correct_guesses = 0
    num_incorrect_guesses = 0
    guess_chars = []

def PlayGame():

    playing = True

    while playing:

        PrintGallows(num_incorrect_guesses)
        print(current_word)
        PrintGuesses()
        AcceptGuess()

        if WordIsGuessed():

            playing = False
    
    if UserRestart() == True:

        GameLoop("Let's play again!")

def PrintGuesses():

    string = "\n"                                           #Add an extra line of space

    if len(guess_chars) > 0:                                #Global list 'guess_chars'

        string += "These letters aren't in the word:\n"

    else:
        string += "Your incorrect guesses will appear here"

    for char in guess_chars:
        string += f" {char}, "

    print(string)

    print(f"Guess Total: {num_correct_guesses + num_incorrect_guesses}  #Correct Guesses: {num_correct_guesses} -- #Incorrect Guesses: {num_incorrect_guesses}\n")

def PrintGallows(num_guesses):

    gallows_list = ["T----T",
                    "|    |",
                    "|",
                    "|",
                    "|",
                    "L___"]
    
    guess_list = ["|    O",
                  "|    |",
                  "|   /|",
                  "|   /|\\",
                  "|   / ",
                  "|   / \\   bruh"]
    
    if num_guesses >= 1:
        gallows_list[2] = guess_list[0]
    if num_guesses == 2:
        gallows_list[3] = guess_list[1]
    if num_guesses == 3:
        gallows_list[3] = guess_list[2]
    if num_guesses >= 4:
        gallows_list[3] = guess_list[3]
    if num_guesses == 5:
        gallows_list[4] = guess_list[4]
    if num_guesses >= 6:
        gallows_list[4] = guess_list[5]
    
    print("\n")
    for line in gallows_list:
        print(line)

    


def AcceptGuess():

    user_inputing = True

    while user_inputing:

        guess = input("What is your guess?: ").lower()

        if len(guess) > 0:
            user_inputing = False

    match_found = current_word.CheckGuess(guess[0])                 #Only using first character

    if match_found:
        global num_correct_guesses
        num_correct_guesses += 1
        
    else:
        global guess_chars

        if not guess[0] in guess_chars:
            guess_chars.append(guess[0])

        global num_incorrect_guesses
        num_incorrect_guesses += 1

def WordIsGuessed():

    guessed = current_word.CheckCompleteness()

    if guessed:
        print(current_word)
        print(f"\nCongrats! The word was {current_word.complete.capitalize()}!")
        print(f"Guess Total: {num_correct_guesses + num_incorrect_guesses}  #Correct Guesses: {num_correct_guesses} -- #Incorrect Guesses: {num_incorrect_guesses}\n")
        return True
    
    else:
        return False
    
def UserRestart():

    response = input("Would you like to play again? (y: play again -- enter: quit)")

    if response.lower() == 'y':
        return True

    else:
        print("Thanks for playing! 'Till next time.")
        return False

GameLoop("Welcome to hang man!")

