#Step 5
#delete line 3 and clear () in line 31 if you cannot utilize the clear function
#used below if using replit, otherwise, keep the code from running
#from replit import clear
from hangman_art import logo
import random
print(logo)

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
#import hangman_words
#use variable hangman_words.word_list instead of word_list is viable
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
#I needed to create a guess list to not penalized against already guessed answers and to see already guessed answers
guess_list = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #use below with replit, otherwise keep the code from running
    #clear()
    if guess in guess_list:
      print("You already guessed this! Try again.")

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #below for debugging
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
      if guess not in guess_list:
        guess_list += guess
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(f"{' '.join(guess_list)}")
    print(stages[lives])
