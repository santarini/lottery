import random
import sys

n = 1
startNumber = input("\nPick 6 numbers from 1 to 47:\n")
numberArray = [int(i) for i in startNumber.split()]
numberArray.sort()
if ((len(numberArray) != len(set(numberArray))) == True):
    print("\nYou entered a duplicate")
    print(numberArray)
elif (len(numberArray) < 6):
    print("\nYou didn't enter enough numbers")
    print(numberArray)
elif (len(numberArray) > 6):
    print("\nYou entered too many numbers")
    print(numberArray)
elif (max(numberArray) > 47):
    print("\nOne or more of your values is too large")
    print(numberArray)
elif (min(numberArray) < 1):
    print("\nOne or more of your values is too small")
    print(numberArray)
else:
    print(numberArray)
    WhiteBalls = random.sample(range(1,48), 6)
    while(numberArray != WhiteBalls):
        WhiteBalls = random.sample(range(1,48), 6)
        WhiteBalls.sort()
        print(WhiteBalls)
        if (numberArray == WhiteBalls):
            print("You won!")
            print("After " + str(n) + " tries")
        else:
            print("You lost " + str(n) + " times")
            n += 1
