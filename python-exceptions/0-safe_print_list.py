#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for element in my_list:
        if count < x:
            try:
                print(element, end='')
                count += 1
            except:
                pass
        else:
            break
    print()
    return count
