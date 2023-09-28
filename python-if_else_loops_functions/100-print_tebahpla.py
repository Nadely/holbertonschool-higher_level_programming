#!/usr/bin/python3
for za in range(122, 96, -1):
    if za % 2 == 1:
        za = za - 32
    print("{}".format(chr(za)), end='')
