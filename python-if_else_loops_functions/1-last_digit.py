#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} ", end='')

if number <= 0:
    last_digit = -int(repr(number)[-1])
else:
    last_digit = int(repr(number)[-1])

if number > 5:
    print(f"is {number} and is greater than 5")
elif number < 6 and number != 0:
    print(f"is {number} and is less than 6 and not 0")
elif number == 0:
    print(f"is {number} and is 0")
