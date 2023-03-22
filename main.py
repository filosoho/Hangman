import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo + '\n\n')

display = []
for _ in range(word_length):
    display += "_"
  
chosen_letter = True

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("\nYou already chose this letter. Try again.\n")
      
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print("--------------------------------------------------------------")
        print(f"The letter '{guess}' is not in this word. You loose a life.")
        print("--------------------------------------------------------------")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.\n")
            print("====================================")
            print(f"\nThe word was {chosen_word}\n")
            print("====================================")
          
    #Join all the elements in the list and turn it into a string.
    print(f"\n{' '.join(display)}")
    
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win!")
    
    print(stages[lives])