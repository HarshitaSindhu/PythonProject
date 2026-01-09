# student_score = [150 , 100 ,45, 35, 86, 789, 543, 5, 98 , 5]
#
# total_exam_score = sum(student_score)
# print(total_exam_score)
# sum = 0
# for i in student_score:
#     sum+=i
# print(sum)
#
# max = student_score[0]
# for i in student_score:
#     if i >max:
#         max = i
# print(max)
#
#
# total = 0
# for i in range (1,101):
#     total = total + i
# print(total)
#
#
#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
import random

# PROJECT - PASSWORD GENERATOR

import random

letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers_list = ['0','1','2','3','4','5','6','7','8','9']
symbols_list = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

password_list = []

for i in range(nr_letters):
    password_list.append(random.choice(letters_list))

for i in range(nr_symbols):
    password_list.append(random.choice(symbols_list))

for i in range(nr_numbers):
    password_list.append(random.choice(numbers_list))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("Your password is:", password)
