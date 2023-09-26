#!/usr/bin/python3
for number in range(10):
    for number2 in range(number, 10):
        if number != number2:
            print("{}{}" .format(number, number2), end=', '
                  if number != 8 or number2 != 9 else "")
print("")
