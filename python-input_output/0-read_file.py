#!/usr/bin/python3
def read_file(filename=""):
    with open(filename = "my_file_0.txt", "r") as file:
        return file.read()
