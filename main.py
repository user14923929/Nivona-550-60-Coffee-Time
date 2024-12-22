import os
import coffees.make
import time

os.system("cls")

balance = 25.00
print(f"Welcome to the coffee machine! Your current balance is ${balance}.")
loop = True

while loop:
    coffee_type = input("What type of coffee would you like? (espresso/latte/cappuccino): ")
    balance = coffees.make.make(coffee_type, balance)
    print(f"Your new balance is {balance}.")
    time.sleep(2)
    if balance <= 0.00:
        print("Sorry, you don't have enough money for any more coffee.")
        time.sleep(2)
        loop = False

    os.system("cls")
    print(f"Your current balance is ${balance}.")