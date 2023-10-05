#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            element1 = my_list_1[i]
            element2 = my_list_2[i]
            if not (isinstance(element1, (int, float)) and isinstance(element2, (int, float))):
                raise TypeError("wrong type")
            if element2 == 0:
                raise ZeroDivisionError("division by 0")
            division_result = element1 / element2
            result.append(division_result)
        except (ZeroDivisionError, TypeError, IndexError) as e:
            print(e)
            result.append(0)
        finally:
            pass
    return result
