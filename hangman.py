import random


def play():

    print("*********************************")
    print("***Welcome to Hangman Game!***")
    print("*********************************")

    lost = False
    win = False
    miss = 0

    words = read_txt()
    secretWord, guessedWords = randomize_word(words)

    print(guessedWords)
    print(secretWord)

    game_conditions(lost, win, miss, secretWord, guessedWords)


def game_conditions(lost, win, miss, secretWord, guessedWords):
    while (not lost and not win):
        guess = input("Guess a letter: ").strip().upper()

        if (guess in guessedWords):
            print("You already guessed {}".format(guess))
        elif (guess not in secretWord):
            miss += 1
            print_hangman(miss)
        else:
            index = 0
            for letter in secretWord:
                if (guess == letter):
                    guessedWords[index] = letter
                index += 1

        lost = miss == 7
        win = "_" not in guessedWords
        print(guessedWords)
        print(miss)

    if (win):
        win_message()
    else:
        lose_message(secretWord)


def randomize_word(words):
    number = random.randrange(0, len(words))

    secretWord = words[number].upper()
    guessedWords = ["_" for letters in secretWord]
    return secretWord, guessedWords


def read_txt():
    document = open("words.txt", "r")

    words = []

    for word in document:
        word = word.strip()
        words.append(word)
    document.close()
    return words


def win_message():
    print("Congrats, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def lose_message(secretWord):
    print("Oh no, you lost!")
    print("The secret word was {}".format(secretWord))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_hangman(miss):
    print("  _______     ")
    print(" |/      |    ")

    if (miss == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (miss == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (miss == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (miss == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (miss == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (miss == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (miss == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    play()
