from utils import clear, dialog
import keyboard
import time

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

from word_counter import word_counter
from number_guess import number_guess
from password_gen import strong_pass_generator
from vid_downloader import download_app


def runScript(script, name: str):
    input()
    while True:
        dialog(name)
        script()

        choice: str = input("\n[y] Back to menu?  ~> ")
        if choice.lower() == "y":
            break


def closeApp():
    clear()
    print("App exited")
    exit()


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
    "Number guess",
    "Password generator",
    "Youtube downloader",
]


def runChoice(choice: int):
    if choice == 0:
        runScript(word_counter, options[choice])
    elif choice == 1:
        runScript(calculator, options[choice])
    elif choice == 2:
        runScript(celsius_to_fahrenheit, options[choice])
    elif choice == 3:
        runScript(fahrenheit_to_celsius, options[choice])
    elif choice == 4:
        runScript(fibo_prog, options[choice])
    elif choice == 5:
        runScript(factorial_prog, options[choice])
    elif choice == 6:
        runScript(is_palindrome, options[choice])
    elif choice == 7:
        runScript(is_prime, options[choice])
    elif choice == 8:
        runScript(rock_paper_scissors, options[choice])
    elif choice == 9:
        runScript(number_guess, options[choice])
    elif choice == 10:
        runScript(strong_pass_generator, options[choice])
    elif choice == 11:
        runScript(download_app, options[choice])


def main():
    cursor: int = 0
    while True:
        clear()

        print("Scripts:\n")

        for index, option in enumerate(options):
            print(f"{">" if cursor==index else " "} {option}")

        print("\nUse arrow keys to select, press [enter] to proced, press [q] to exit")

        while True:
            time.sleep(0.2)
            key = keyboard.read_key()

            if key == "up":
                if 0 < cursor:
                    cursor -= 1
                else:
                    continue
            elif key == "down":
                if cursor < len(options) - 1:
                    cursor += 1
                else:
                    continue
            elif key == "q":
                closeApp()
            elif key == "enter":
                runChoice(cursor)
            else:
                continue

            if key is not None:
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        closeApp()
