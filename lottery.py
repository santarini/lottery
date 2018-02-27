import random

def Lottery():
    startNumber = input("\nPick 5 numbers from 1 to 69:\n")
    numberArray = [int(i) for i in startNumber.split()]
    numberArray.sort()
    if ((len(numberArray) != len(set(numberArray))) == True):
        print("\nYou entered a duplicate")
        print(numberArray)
        Lottery()
    elif (len(numberArray) < 5):
        print("\nYou didn't enter enough numbers")
        print(numberArray)
        Lottery()
    elif (len(numberArray) > 5):
        print("\nYou entered too many numbers")
        print(numberArray)
        Lottery()
    elif (max(numberArray) > 69):
        print("\nOne or more of your values is too large")
        print(numberArray)
        Lottery()
    elif (min(numberArray) < 1):
        print("\nOne or more of your values is too small")
        print(numberArray)
        Lottery()
    else:
        print(numberArray)
    CheckMatch(numberArray)

def Draw():
    WhiteBalls = random.sample(range(1,70), 5)
    #PowerBall = random.sample(range(1,27), 1)
    WhiteBalls.sort()
    print(WhiteBalls)
    #print(PowerBall)

def CheckMatch(numberArray):
    if (numberArray == [1, 2, 3, 4, 5]):
        print("You won!")

Lottery()
