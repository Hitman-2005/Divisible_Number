# Simple Python Checking if a number can be divided or not with color as output

from colorama import Fore

number = int(input("Number: "))

for x in range(1, 11):
    if number % x == 0:
        print(Fore.GREEN + f"{number} is divisible by {x}")
    else:
        print(Fore.RED + f"{number} is not divisible by {x}")
