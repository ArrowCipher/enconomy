import random

# Define the game's constants.
NUM_PLAYERS = 1
STARTING_MONEY = 100
GOODS = ["wheat", "corn", "soybean", "Burger"]
PRICES = {"wheat": 10, "corn": 20, "soybean": 30, "Burger": 25}

# Create a class for each type of player.
class Player:
    def __init__(self, name):
        self.name = name
        self.money = STARTING_MONEY
        self.goods = []
        self.mining_skill = 1
        self.bank = 0

    def buy_good(self, good, quantity):
        price = PRICES[good] * quantity
        if self.money >= price:
            self.goods.append((good, quantity))
            self.money -= price
        else:
            print("You don't have enough money.")

    def sell_good(self, good, quantity):
        price = PRICES[good] * quantity
        self.money += price
        self.goods.remove((good, quantity))

    def earn_money(self, amount):
        self.money += amount

    def mine(self):
        amount = random.randint(10, 100) * self.mining_skill
        print("You earned $", amount, "for mining.")
        self.earn_money(amount)

# Create a main loop that runs the game.
def main():
    player = Player("Player 1")

    while True:
        # The player can buy or sell goods, or earn money by mining.
        action = input("What do you want to do? (buy, sell, mine, bank, quit): ")
        if action == "buy":
            good = input("What good do you want to buy? ")
            quantity = int(input("How many units do you want to buy? "))
            player.buy_good(good, quantity)
        elif action == "sell":
            good = input("What good do you want to sell? ")
            quantity = int(input("How many units do you want to sell? "))
            if good in player.goods:
                price = PRICES[good] * quantity
                player.money += price
                player.goods.remove((good, quantity))
                print(f"You sold {quantity} units of {good} for ${price}.")
            else:
                print(f"You don't have any {good}.")
        elif action == "mine":
            amount = random.randint(10, 100) * player.mining_skill
            print("You earned $", amount, "for mining.")
            player.earn_money(amount)
        elif action == "bank":
            amount = int(input("How much money do you want to deposit? "))
            player.money -= amount
            player.bank += amount
            print(f"You deposited ${amount} into your bank account.")
        elif action == "withdraw":
            amount = int(input("How much money do you want to withdraw? "))
            if amount <= player.bank:
                player.money += amount
                player.bank -= amount
                print(f"You withdrew ${amount} from your bank account.")
            else:
                print("You don't have enough money in your bank account.")
        elif action == "quit":
            break

        # Update the game's state.
        print(f"You have ${player.money} dollars.")
        print(f"Your bank balance is ${player.bank} dollars.")

if __name__ == "__main__":
    main()
