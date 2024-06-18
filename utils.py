import os
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def dialog(message):
    clear()
    length = len(message) + 4

    print("=" * length)
    print(f"= {message} =")
    print("=" * length)

    time.sleep(1)


def invalidInput(choice):
    dialog(f"[{choice}]: is not a valid input")


def validateInput(input: str):
    output = True

    try:
        int(input)
    except ValueError:
        invalidInput(input)
        output = False

    return output
