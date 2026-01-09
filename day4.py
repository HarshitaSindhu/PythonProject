import random
# random_integer = random.randint(1,100)
# print(random_integer)
# random_number_0_to_1=random.random()
# print(random_number_0_to_1)
#
# random_number_0_to_10=random.random()*10
# print(random_number_0_to_10)


#Random element from the list
import random
friends =["Ayushi" , "Jasmeet" , "Mitali" ,"Khushi", "Siya"]

print(random.choice(friends))


# DAY4 PROJECT

import random

user_choice = int(input("Enter your choice ? 0 for rock, 1 for scissors, 2 for paper : "))
computer_choice = random.randint(0, 2)

print(f"Computer's choice is: {computer_choice}")
print(f"User's choice is: {user_choice}")

if computer_choice == user_choice:
    print("Tie")

elif computer_choice == 0:  # Rock
    if user_choice == 1:
        print("Computer wins")
    else:
        print("User wins")

elif computer_choice == 1:  # Scissors
    if user_choice == 2:
        print("Computer wins")
    else:
        print("User wins")

else:  # Paper
    if user_choice == 0:
        print("Computer wins")
    else:
        print("User wins")
