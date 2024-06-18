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


def validateInput(input: str):
    output = True

    try:
        int(input)
    except ValueError:
        invalidInput(input)
        output = False

    return output
