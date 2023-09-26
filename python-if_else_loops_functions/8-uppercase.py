#!/usr/bin/python3
def uppercase(str):
    letter_uppercase = 0
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            letter_uppercase = ord(letter) - 32
        else:
            letter_uppercase = ord(letter)
        print("{}".format(chr(letter_uppercase)), end="")
    print("")
