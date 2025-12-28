import random
from hangman_words import word_list
from hangman_art import stages, logo
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letters = []

while not game_over:
    guess = input("Enter your guess: ")
    if guess in correct_letters:
        print(f"{guess} is in the correct position")

    display=""
    for letter in chosen_word:
        if letter== guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess not in chosen_word:
        lives-=1
        print(f"you're {guess} guess is not in the word, you have {lives} lives left")
        if lives == 0:
            game_over = True
            print("You Lose!")
    if "_" not in display:
        game_over=True
        print("you have won")
    print(stages[lives])