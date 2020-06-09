#! /usr/bin/python3

print("Tthis is a Python script that will countdown from the user input number")
input = int(raw_input("Enter the countdown number: "))

while input > -1:
    print (input)
    input -= 1

print("To infinity and beyond!")
