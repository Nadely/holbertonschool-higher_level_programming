#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """Public instance method that prints the list,
        but sorted (ascending sort)"""

    def print_sorted(self):
        for item in self:
            if not isinstance(item, int):
                raise TypeError('Not all elements in the list are integers')
        print(sorted(self))
