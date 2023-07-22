import hangman
import guess


def choose_game():
    print("*********************************")
    print("*******Choose Your Game!*******")
    print("*********************************")

    print("(1) Hangman (2) Guess")

    game = int(input("Which Game? "))

    if (game == 1):
        print("Playing Hangman")
        hangman.play()
    elif (game == 2):
        print("Playing Guess")
        guess.play()


if (__name__ == "__main__"):
    choose_game()
