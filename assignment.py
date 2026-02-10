# Ask the user for input
# We wrap it in int() because input() always returns a string
from traceback import print_tb

try:
    number = int(input("Enter a random number: "))

    # Check if the remainder is 0
    if number == 0 :
        print("number is neutral")

    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")
