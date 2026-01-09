# colours ={
#     "apple":"red",
#     "banana":"green",
#     "pear":"blue",
# }
# colours["mango"] = "yellow"
# print(colours)
#
#
# wipe an existing dictionary
# colours={}
# print(colours)
#
#
# # edit an item in dictionary
#
# colours["banana"]="yellow"
#
# for i in colours:
#     print(i + ":"+colours[i])
#
#
#     student_scores = {
#         'Harry': 88,
#         'Ron': 78,
#         'Hermione': 95,
#         'Draco': 75,
#         'Neville': 60
#     }
#
#     student_grades = {}
#
#     for student in student_scores:
#         score = student_scores[student]
#
#         if score >= 91 and score <= 100:
#             student_grades[student] = "Outstanding"
#         elif score >= 81 and score <= 90:
#             student_grades[student] = "Exceeds Expectations"
#         elif score >= 71 and score <= 80:
#             student_grades[student] = "Acceptable"
#         else:
#             student_grades[student] = "Fail"
#
#     print(student_grades)


# Nested List in Dictionary
#
# travel_log ={
#     "France":["Paris ", "Lille" , "dijon"],
#     "India":["Jaipur" , "Delhi"]
# }
#
#
# print(travel_log["France"][1])



# *****SECRET AUCTION PROGRAM*****


# bids={}
# bids_more=True
# while bids_more:
#
#     bidder = input("Enter your name: ")
#     bid_price = int(input("Enter your bid price: ₹"))
#     bids[bidder]=bid_price
#
#     more_bidder = input("Are there more bidders? Yes or No: ").lower()
#     if more_bidder == "no":
#         bids_more = False
#
#     else:
#        print("\n"*100)
#
# highest_bidd = 0
# winner=""
# for bidder in bids:
#     if bids[bidder]>highest_bidd:
#         highest_bidd = bids[bidder]
#         winner = bidder
#
# print("🏆 Auction Result 🏆")
# print(f"Winner: {winner}")
# print(f"Winning Bid: ₹{highest_bidd}")


def find_highest_bidder(bidding_dictionary):
    highest_bidd = 0
    winner = ""
    for bidder in bidding_dictionary :
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidd :
            highest_bidd = bid_amount
            winner = bidder
    print("🏆 Auction Result 🏆")
    print(winner)   


bids={}
continue_bidding =True
while continue_bidding :
    name = input("What is your name? ")
    price = int(input("What is your price? "))
    bids[name] = price
    should_continue = input("Would you like to continue? (y/n) ")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*100)





