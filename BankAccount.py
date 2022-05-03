class BankAccount:
    Bank_name = "paypy"

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_balance(self):
        print("Current balance is :", self.balance)

    def greet(self, name):
        print("welcome", name)


def main():
    account1 = BankAccount()
    account1.greet("michal")
    account2 = BankAccount(4000)
    account2.greet("amir")
    account2.deposit(1)
    account1.deposit(1)
    account1.print_balance()
    account2.print_balance()
    eyal = BankAccount(7000)
    eyal.deposit(1200)
    eyal.withdraw(200)
    eyal.print_balance()
    print(BankAccount.Bank_name)


main()
