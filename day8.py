# def life_in_weeks(age):
#     left_age = 90 - age
#     answer = left_age * 52
#     print(f"You have {answer} weeks left.")
#
# agee = int(input("enter the age : "))
# life_in_weeks(agee)
#
# def calculate_love_score(name1, name2):
#     TRUE_count = 0
#     LOVE_count = 0
#
#     TRUE = ['t', 'r', 'u', 'e']
#     LOVE = ['l', 'o', 'v', 'e']
#
#     resultName = (name1 + name2).lower()
#
#     for i in resultName:
#         if i in TRUE:
#             TRUE_count += 1
#         if i in LOVE:
#             LOVE_count += 1
#
#     print(f"{TRUE_count}{LOVE_count}")
#
# calculate_love_score("Kanye West", "Kim Kardashian")


# Caesar cipher PROJECT
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']


# def encrypt(original_text, key):
#     cipher_text = ""
#     for letter in original_text:
#         if letter in alphabet:
#             shifted_position = alphabet.index(letter) + key
#             shifted_position %= len(alphabet)
#             cipher_text += alphabet[shifted_position]
#         else:
#             cipher_text += letter
#     print(f"encoded text: {cipher_text}")
#
# def decrypt(cipher_text, key):
#     original_text = ""
#     for letter in cipher_text:
#         if letter in alphabet:
#             shifted_position = alphabet.index(letter) - key
#             shifted_position %= len(alphabet)
#             original_text += alphabet[shifted_position]
#         else:
#             original_text += letter
#     print(f"decoded text: {original_text}")
def caesar(original_text, key, encode_or_decode):
    output_text = ""

    # reverse shift ONCE for decode
    if encode_or_decode == "decode":
        key *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + key
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"{encode_or_decode}d text: {output_text}")


    print(f"{encode_or_decode}d text: {output_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt and type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to play again? ").lower()
    if restart == "no":
        should_continue = False
