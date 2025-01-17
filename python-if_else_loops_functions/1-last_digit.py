#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
print(f"Last digit of {number} is {last_digit}", end="")

if number > 5:
    print (number "and is than 5")
elif number == 0:
    print (number "and is 0")
else if number < 6 and number != 0:
    print (number "and is less than 6 and not 0")
