import random


def play():

    print("*********************************")
    print("Welcome to Guess!")
    print("*********************************")

    secretNumber = random.randrange(1, 101)
    numbersTry = 0
    points = 1000

    print("Choose a dificulty level")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Dificulty: "))

    if (level == 1):
        numbersTry = 20
    elif (level == 2):
        numbersTry = 10
    else:
        numbersTry = 5

    for round in range(1, numbersTry + 1):
        print("Try {} off {}".format(round, numbersTry))

        guessStr = input("Type a number between 1 and 100: ")
        print("You typed ", guessStr)
        guess = int(guessStr)

        if (guess < 1 or guess > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        win = guess == secretNumber
        greater = guess > secretNumber
        lower = guess < secretNumber

        if win:
            print("You got it and got {} points!".format(points))
            break
        else:
            if greater:
                print("You missed, Your guess was greater than the secret number.")
            elif (lower):
                print("You missed, Your guess was lower than the secret number.")
            lostPoints = abs(secretNumber - guess)
            points = points - lostPoints

    print("Game Over")


if (__name__ == "__main__"):
    play()
