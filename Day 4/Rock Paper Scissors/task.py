import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice =int(input("what do you choose? rock 0, paper 1 , or scissors 2?"))
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(game_images[computer_choice])

if user_choice >= 3 or computer_choice < 0:
    print("invalid choice")
elif user_choice == 2 and computer_choice == 0:
    print("you lose")
elif user_choice == 0 and computer_choice == 2:
    print(f"you win")
elif user_choice < computer_choice:
    print(f"you lose")
elif user_choice > computer_choice:
    print(f"you win")
elif user_choice == computer_choice:
    print(f"its a draw")
