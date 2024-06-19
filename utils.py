import os
import time
from urllib.parse import urlparse


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def dialog(message):
    clear()
    length = len(message) + 4

    print("=" * length)
    print(f"= {message} =")
    print("=" * length)
    print()


def invalidInput(choice):
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


def is_valid_url(url: str) -> bool:
    parsed_url = urlparse(url)

    return parsed_url.scheme and parsed_url.netloc
