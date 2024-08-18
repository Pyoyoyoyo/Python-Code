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

#Write your code below this line 👇

player_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
rps = [rock, paper, scissors]
if player_number >= 3 or player_number < 0:
  print("You typed a invalid number, you lose!")
else:
  if player_number == 0 or player_number == 1 or player_number == 2:
    com_number = random.randint(0,2)
    if player_number > com_number and player_number != 0 and com_number != 2:
      print(rps[player_number])
      print(rps[com_number])
      print("player wins!")
    elif player_number > com_number and player_number != 2 and com_number != 0:
      print(rps[player_number])
      print(rps[com_number])
      print("player wins!")
    elif player_number == com_number:
      print(rps[player_number])
      print(rps[com_number])
      print("Draw.")
    
    else:
      print(rps[player_number])
      print(rps[com_number])
      print("you lose.")
  
  else:
    player_number = input("Wrong value! What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
  