class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Final Balance:", self.balance)


# Create a bank account
account = BankAccount("alex", 5000)

# Deposit money
account.deposit(2000)

# Withdraw money
account.withdraw(3000)

# Try to withdraw more than the balance
account.withdraw(5000)

# Display final balance
account.display_balance()