import time

def make(type, balance):
    if type == "espresso":
        if balance < 1.50:
            print("Sorry, you don't have enough money for an espresso.")
            return balance
        else:
            print("Making espresso...")
            time.sleep(2)
            print("Espresso is ready! Enjoy!")
            return balance - 1.50
    elif type == "latte":
        if balance < 2.50:
            print("Sorry, you don't have enough money for a latte.")
            return balance
        else:
            print("Making latte...")
            time.sleep(2)
            print("Latte is ready! Enjoy!")
            return balance - 2.50
    elif type == "cappuccino":
        if balance < 3.00:
            print("Sorry, you don't have enough money for a cappuccino.")
            return balance
        else:
            print("Making cappuccino...")
            time.sleep(2)
            print("Cappuccino is ready! Enjoy!")
            return balance - 3.00