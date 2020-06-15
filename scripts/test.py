#! /usr/bin/python3

print("This is a Python script that will countdown from the user input number.")
input = int(raw_input("Please enter a number to countdown from: "))

while input > -1:
    print (input)
    input -= 1

print("To infinity and beyond!")
