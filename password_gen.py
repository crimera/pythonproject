import string
import time
import keyboard
from utils import clear, validateInput, dialog
import random


def runChoice(options):
    input()

    length = input("How long do you want your password to be: ")

    if not validateInput(length):
        return

    length = int(length)

    letters = ""

    for option in options:
        enabled = option["enabled"]
        name = option["name"]

        if not enabled:
            continue

        if name == "Letters":
            letters += string.ascii_letters
        elif name == "Digits":
            letters += string.digits
        elif name == "Special characters":
            letters += string.punctuation

    password = []

    for i in range(length):
        password.append(random.choice(letters))

    print(f"Your password is: {"".join(password)}")


def strong_pass_generator():
    cursor = 0

    options = [
        {"enabled": True, "name": "Letters"},
        {"enabled": True, "name": "Digits"},
        {"enabled": True, "name": "Special characters"},
    ]

    run = True
    while run:
        clear()

        dialog("Password generator")

        for index, option in enumerate(options):
            print(
                f"{">" if index == cursor else " "} [{"x" if option["enabled"] else " "}] {option["name"]}"
            )

        print(
            "\nUse arrow keys to select, press [space] to toggle option, press [enter] proceed, press [q] to exit"
        )

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
            elif key == "enter":
                runChoice(options)
                run = False
            elif key == "space":
                options[cursor]["enabled"] = not options[cursor]["enabled"]
            else:
                continue

            if key is not None:
                break


if __name__ == "__main__":
    strong_pass_generator()
