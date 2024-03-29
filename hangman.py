import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) # randomly choose something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # user's previous guesses

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters)) 
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'

        # current word (W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: # if current letter is in the alphabet but not used yet
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            
            else:
                lives -= 1
                print('\nYour letter', user_letter, 'is not in the word.')
        
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Please try again')
        
        else:
            print('\nYou did not type a valid character.')
    
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Congrats! You guess the word', word, '!')

hangman()