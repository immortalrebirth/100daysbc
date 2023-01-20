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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
images = [rock, paper, scissors]
choices = ["rock","paper","scissors"]
cpuchoice = random.randint(0,2)
print(f"You chose {choices[choice]}")
print(images[choice])
if cpuchoice == 0:
  print("Computer chose rock.")
  print(rock)
  if choice == 0:
    print("IT'S A TIE!")
  if choice == 1:
    print("YOU WON!")
  if choice == 2:
    print("YOU LOST!")
elif cpuchoice == 1:
  print("Computer chose paper.")
  print(paper)
  if choice == 0:
    print("YOU LOST!")
  if choice == 1:
    print("IT'S A TIE!")
  if choice == 2:
    print("YOU WON!")
elif cpuchoice == 2:
  print("Computer chose scissors.")
  print(scissors)
  if choice == 0:
    print("YOU WON!")
  if choice == 1:
    print("YOU LOST!")
  if choice == 2:
    print("IT'S A TIE!")

