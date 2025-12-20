# # subscripting
# print("HELLO"[-2])
# print("HELLO"[4])
#
# #String
# print("123"+"456 ")
#
# #Integer
# print(123+45)
#
# # LArge Integer
# print(124_45_56789)

#Float
# print(3.55786)

#Boolean
# print(True)
# print(False)
#
# print(5/3)
# print(5//3)
#
# name = "Harshita"
# age  = 20
# print(f"{name}'s age is {age} years old.")


# PROJECT-2

print("Welcome to the tip calculator!")
total_bill = int(input("What is the total bill? "))
tip  = int(input("How much tip would you like to give? "))
split = int(input("How many people to split the bill? "))
pay_amount= (total_bill+(tip/100)*total_bill)/split
print(pay_amount)