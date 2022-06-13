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

you=int(input("what do you choose? Type 0 for rock , 1 for paper or 2 for scissors.") )
computer=random.randint(0,2)

game_images=[rock,paper,scissors]
print("user_choice is :- ")
print(game_images[you])


Computer=random.randint(0,2)
print("computer choice is :- ")
print(game_images[computer])

if(you<0 or computer>4):
  print("invaild values")
if(you==0):
  if(computer==0):
      print("Tie no winner")
  elif(computer==1):
      print("computer wins")
  elif(computer==2):
      print("you win")
if(you==1):
  if(computer==1):
      print("no winner Tie")
  elif(computer==2):
      print("computer wins")
  elif(computer==0):
      print("you win")
if(you==2):
  if(computer==2):
      print("Tie")
  elif(computer==0):
      print(" computer wins")
  elif(computer==1):
      print("You choose  you win")

