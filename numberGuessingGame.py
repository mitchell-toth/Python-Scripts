import random

def guessingGame():
    startingNumber = int(input("What should be the lowest number possible? --> "))
    endingNumber = int(input("What should be the highest number possible? --> "))
    numGuesses = int(input("How many guesses will you be allowed? --> "))
    if numGuesses <= 0 or startingNumber >= endingNumber:
        print("Invalid entries. Try again...")
        print()
        guessingGame()
        
    magicNumber = random.randrange(startingNumber, endingNumber+1)
    print("You are to guess a number between",startingNumber,"and",endingNumber,"(inclusive) in",numGuesses,"guesses or less!")
    print()
    for guess in range(numGuesses):
        userGuess = int(input("Enter your guess: "))
        if userGuess < startingNumber or userGuess > endingNumber:
              print("Invalid number. You lose a guess!")
        elif userGuess == magicNumber:
            print("You guessed it!")
            break
        elif userGuess > magicNumber:
                print("HIGH guess")
        elif userGuess < magicNumber:
                print("LOW guess")
    if guess == numGuesses-1 and userGuess != magicNumber:
        print("You ran out of guesses! Better luck next time!")
        print()
    else:
        print("Good job!")
        print()
    userDesire = input('Type: "Play again" to play another round! --> ')
    if userDesire == "Play again":
        guessingGame()
    else:
        print('Okay. Type "main()" if you ever wish to play again!')


def main():
    startGame = input('Type: "Play" if you wish to play the guessing game! --> ')
    yes = "Play"
    if startGame == yes:
        guessingGame()
    else:
        print("Maybe later then.")
        print()
        main()


main()

                  
            
