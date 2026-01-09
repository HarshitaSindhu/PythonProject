# import random
# word_list = ["aardvark" , "baboon" , "camel"]
# guess  = random.choice(word_list)
# print(guess)
# guess_letter = input("Guess a letter: ").lower()
# # for i in range(0,len(guess)):
# #     if guess[i] == guess_letter:
# #         print("right")
# #     else:
# #         print("wrong")
# #
#
#
# # display =""
# # for i in guess:
# #     if i==guess_letter:
# #         display += guess_letter
# #     else:
# #         display += '_'
# # print(display)
#
# placeholder =""
# for i in range(0,len(guess)):
#    placeholder += '_'
# print(placeholder)
# game_over = False
# correct_letters=[]
# while not game_over:
#     guess_letter = input("Guess a letter: ").lower()
#     display = ""
#     for i in guess:
#         if i == guess_letter:
#             display += guess_letter
#             correct_letters.append(guess_letter)
#         elif letter in correct_letters:
#             display+= guess_letter
#         else:
#             display += '_'
#     print(display)
#     if "_" not in display:
#         game_over = True
#         print("You Win!")





import random

word_list = ["aardvark", "baboon", "camel"]
guess = random.choice(word_list)
print(guess)
lives = 6

placeholder = ""
for i in range(len(guess)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

display = placeholder

while not game_over:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter in correct_letters:
        print(f"You have already guessed the letter {guess_letter}")
    if guess_letter not in guess and guess_letter not in correct_letters:
        lives -= 1
        print(f"Wrong guess. Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You Lose!")

    if guess_letter not in correct_letters:
        correct_letters.append(guess_letter)

    new_display = ""
    for i in guess:
        if i in correct_letters:
            new_display += i
        else:
            new_display += "_"

    display = new_display
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")
