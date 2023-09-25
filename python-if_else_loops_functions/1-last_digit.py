#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} ", end='')

if number <= 0:
    last_digit = -int(repr(number)[-1])
else:
    last_digit = int(repr(number)[-1])

elif last_digit == 0:
    print(f"is {last_digit} and is 0")
if last_digit < 6 and last_digit != 0:
    print(f"is {last_digit} is less than 6 and not 0")
elif last_digit > 5:
    print(f"is {last_digit} and is greater than 5")
