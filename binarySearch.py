#Mitchell Toth
#10/6/2020
#A quick binary search guess-the-number program

DEBUG = False

def getInteger(minVal, maxVal):
    while True:
        userNum = input("Please type an integer between " + str(minVal) + " and " + str(maxVal) + " --> ")
        try:
            userNum = int(userNum)
            if userNum < minVal or userNum > maxVal:
                raise
        except:
            print("Invalid! Try again!", end=" ")
            continue
        return userNum
    

def deduceUserNum(minVal, maxVal, answer):
    iters = 0
    while (minVal != maxVal):
        iters += 1
        guess = minVal + (maxVal-minVal)//2
        if guess > answer:
            maxVal = guess-1
        elif guess < answer:
            minVal = guess+1
        else:
            break
        if DEBUG:
            print("Guess:", str(guess) + ", Iters:", iters)
            input() #Press Enter to continue
    guess = minVal + (maxVal-minVal)//2
    print("The computer found your number,", guess, ", in", iters, "iterations!")
    return guess


def main():
    minVal = 0
    maxVal = 100
    keepGoing = True
    while keepGoing:
        answer = getInteger(minVal, maxVal)
        deduceUserNum(minVal, maxVal, answer)
        keepGoing = input("Go again? Y/N --> ").upper() == "Y"
        print()

main()
    
