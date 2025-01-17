#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE

    if number > 0:
        print(f"{number} is positive"); #si number est plus grand que zéro on afiiche qu'il est positive.

    elif number == 0:
        print(f"{number} is zero"); #si number est egal a zéro on affiche qu'il est nul.

    else:
        print(f"{number} is negative"); #sinon on affiche qu'il est négative.
