import random


def choose_word():
    words = ["apple", "banana", "orange", "strawberry", "grapes"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display = display_word(word_to_guess, guessed_letters)
        print("\nCurrent word:", display)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            if display_word(word_to_guess, guessed_letters) == word_to_guess:
                print("\nCongratulations! You guessed the word:", word_to_guess)
                break
            else:
                print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess. Attempts remaining:", attempts)

    if attempts == 0:
        print("\nSorry, you're out of attempts. The word was:", word_to_guess)


hangman()
