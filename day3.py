# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Type y for Yes and n for No: ").lower()
#     if wants_photo == "y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# PROJECT-3
#
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# bill = 0
# if size == "S":
#     bill+=15
#     if pepperoni == "Y":
#         bill+=2
# elif size == "M":
#     bill+=20
#     if pepperoni == "Y":
#         bill+=3
# else:
#     bill+=25
#     if pepperoni == "Y":
#         bill+=3
# if extra_cheese == "Y":
#     bill+=1
# print(f"Your final bill is ${bill}")



# PROJECT-Treasure Island

print("Welcome to Treasure Island ")
direction = input("left or right : ")


if direction == "left":
    action = input("enter your action : swim or wait")
    if action == "wait":
        door = input("enter your door :  Red , Blue , Yellow")

        if door == "Yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")

