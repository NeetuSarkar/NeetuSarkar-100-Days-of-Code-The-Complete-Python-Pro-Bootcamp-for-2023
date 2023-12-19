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

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]

user_choose = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
if user_choose >= 3 or user_choose < 0:
  print("You typed a invalid number your loose")
else:
  print(f"User Choose: {game_images[user_choose]}")
  
  computer_choose = random.randint(0, 2)
  print(f"Computer choose: {game_images[computer_choose]}")
  
  if user_choose == 0 and computer_choose == 2:
      print("You win!")
  elif computer_choose == 0 and user_choose == 2:
      print("You lose!")
  elif computer_choose > user_choose:
      print("You lose!")
  elif user_choose > computer_choose:
      print("You win!")
  elif computer_choose == user_choose:
      print("It's a draw!")
  
  