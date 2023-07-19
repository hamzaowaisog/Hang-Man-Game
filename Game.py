#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from hangman_guessing import guess_list
guessing_word = random.choice(guess_list).lower()
word_letter = len(guessing_word)
game_over = False
tries = word_letter
from hangman_life import game_name
print(game_name)

result =[]
for _ in range(word_letter):
    result+='_'

while not game_over:
    user_guess = input("Guess a letter: ")

    if user_guess in result:
        print("The letter you have guessed is "+ user_guess)

    for position in range (word_letter):
        letter = guessing_word[position]
        if letter == user_guess:
            result[position] = letter
    if user_guess not in guessing_word:
        print("You have guessed "+user_guess + " This letter is not in the word you lose a try")
        tries -=1

        if tries == 0:
            game_over = True
            print("Game Over")
            print("The word is "+guessing_word)
            

    print(f"{' '.join(result)}")
             
    if '_' not in result:
        game_over = True
        print("You are a winner , Congratulations")
        
    from hangman_life import lives
    print(lives[tries])


# In[ ]:




