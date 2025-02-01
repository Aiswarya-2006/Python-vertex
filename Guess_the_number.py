import random
user_num= int (input("Enter 0 or 1: "))
computer_num=random.randint(0,1)
#print(computer_num)
if(user_num == computer_num):
	print("Correct!")
else:
	print("Wrong! Try again")
