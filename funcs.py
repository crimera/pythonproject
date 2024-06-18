import random
from utils import validateInput


# Calculator
def calculator():
    operation = input("Choose operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        print(f"Result: {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1 * num2}")
    elif operation == "/":
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid operation")


# Temperature Converter
def celsius_to_fahrenheit():
    num = input("Enter celcius: ")

    if not validateInput(num):
        return

    num = int(num)

    print(f"{num} in fahrenheit is {(num * 9 / 5) + 32}")


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Fibonacci Sequence
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def fibo_prog():
    num = input("Enter a number: ")

    if not validateInput(num):
        return

    num = int(num)

    print(f"{fibonacci(num)}")


# Factorial Calculator
def factorial(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_prog():
    num = input("Enter a number: ")

    if not validateInput(num):
        return

    print(f"{num} factorial is: {factorial(int(num))}")


# Palindrome Checker
def is_palindrome():
    inpt = input("Enter a word or a sentence: ")

    inpt = inpt.strip()

    result = inpt == inpt[::-1]

    print(f"{inpt} is {"" if result else "not "}a palindrome")


# Prime Number Checker
def is_prime():
    n = input("Enter a number: ")
    is_prime = True

    if not validateInput(n):
        return

    n = int(n)

    if n <= 1:
        is_prime = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False

    print(f"{n} is {"" if is_prime else "not "}a prime number")


# Rock, Paper, Scissors
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        print(f"You win! Computer chose {computer_choice}.")
    else:
        print(f"You lose! Computer chose {computer_choice}.")
