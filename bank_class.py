
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, name):
        self.balance = initial_amount
        self.name = name
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try: 
            print('\n**********\n\nBeginning Transfer.. ')
            self.viable_transaction(amount) 
            self.withdraw(amount) 
            account.deposit(amount) 
            print('\nTransfer complete! \n\n**********')
        except BalanceException as error: 
            print(f'\nTransfer interrupted.  {error}')

sanjay = BankAccount(1000, "sanjay") # input data of user 1
abi = BankAccount(2000, "abi")       # input data of user 2

sanjay.get_balance()                 # balance
abi.get_balance()

abi.deposit(500)                     # deposit

sanjay.withdraw(10000)               # withdraw
abi.withdraw(10)

sanjay.transfer(10000, abi)          # transfer
sanjay.transfer(100, abi)
