from utils import clear, invalidInput, validateInput
import random


def number_guess():
    irange = input("Range, 1 to: ")
    guesses = input("How many guesses: ")

    if not validateInput(irange):
        return
    irange = int(irange)

    if not validateInput(guesses):
        return
    guesses = int(guesses)

    clear()

    if guesses == 0:
        invalidInput(0)

    num = random.randint(1, irange)

    if not validateInput(num):
        return

    num = int(num)

    for i in range(1, guesses):
        guess = input("Enter your guess: ")
        print()

        if not validateInput(guess):
            continue

        guess = int(guess)

        if int(guess) == num:
            print(f"You win, the number is {num}")
            return

        print(
            f"Beep... boop... wrong number. You only have {guesses-i} guesses remaining",
        )

        print(f"Try something {"higher" if num>guess else "lower"}")

        if guesses - i == 0:
            return

    print(f"You ran out of guesses, The number is {num}")
