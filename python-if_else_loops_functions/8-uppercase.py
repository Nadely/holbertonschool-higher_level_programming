#!/usr/bin/python3
letter_uppercase = 0
def uppercase(str):
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            letter_uppercase = ord(letter) - 32
        else:
            letter_uppercase = ord(letter)
        print("{}".format(chr(letter_uppercase)), end="")
    print("")
