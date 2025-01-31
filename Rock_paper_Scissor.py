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
game = [rock,paper,scissors]
comp_input=random.choice(game)


user_input=int(input("Enter 1 for rock, 2 for paper and 3 for scissors: "))
print("Computer's choice:")
print(comp_input)
print("Your choice:")
if(user_input==1):
    print(rock)
elif(user_input == 2):
    print(paper)
elif (user_input ==3):
    print(scissors)

if ( (user_input ==1 and comp_input == rock )or( user_input==2 and comp_input==paper) or (user_input==3 and comp_input==scissors) ):
    print("Draw!")
elif ((user_input==1 and comp_input==scissors) or (user_input==2 and comp_input==rock) or (user_input==3 and comp_input==paper)):
    print("You win!")
elif((user_input==1 and comp_input==paper) or(user_input ==2 and comp_input==scissors)or (user_input ==3 and comp_input==rock)):
    print("You lose!")
else:
    print("Invalid Input")