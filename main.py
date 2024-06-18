from word_counter import word_counter
from utils import clear, invalidInput
from number_guess import number_guess

from funcs import (
    calculator,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    fibo_prog,
    factorial_prog,
    is_palindrome,
    is_prime,
    rock_paper_scissors,
)


def runScript(script):
    while True:
        clear()
        script()

        choice: str = input("\n[y] Back to menu?  ~> ")
        if choice.lower() == "y":
            break


if __name__ == "__main__":
    while True:
        clear()

        print("Scripts:\n")
        options = [
            "Count words",
            "Calculator",
            "Celcsius to fahrenheit",
            "Fahrenheit to celsius",
            "Fibonacci",
            "Factorial",
            "Palindrome checker",
            "Prime checker",
            "Rock paper scissors",
            "Rumber guess",
        ]

        for index, option in enumerate(options):
            print(f"[{index+1}] {option}")

        choice = input("\ninput ~> ")

        try:
            choice = int(choice)
        except ValueError:
            invalidInput(choice)
            continue

        if choice > len(options):
            invalidInput(choice)
            continue
        elif choice == 1:
            runScript(word_counter)
        elif choice == 2:
            runScript(calculator)
        elif choice == 3:
            runScript(celsius_to_fahrenheit)
        elif choice == 4:
            runScript(fahrenheit_to_celsius)
        elif choice == 5:
            runScript(fibo_prog)
        elif choice == 6:
            runScript(factorial_prog)
        elif choice == 7:
            runScript(is_palindrome)
        elif choice == 8:
            runScript(is_prime)
        elif choice == 9:
            runScript(rock_paper_scissors)
        elif choice == 10:
            runScript(rock_paper_scissors)
