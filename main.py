from word_counter import word_counter
from spotdl import download_from_spotify
import os
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def dialog(message):
    length = len(message) + 4

    print("=" * length)
    print(f"= {message} =")
    print("=" * length)


def invalidInput(choice):
    clear()
    dialog(f"[{choice}]: is not a valid input")
    time.sleep(1)


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
        options = ["Count words"]

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
