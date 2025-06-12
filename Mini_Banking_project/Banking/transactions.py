# from Banking.account import BankAccount, SavingsAccount, CurrentAccount
def deposit(account, amount):
    if amount > 0:
        account.deposit(amount)
    else:
        print("Invalid deposit amount.")

def withdraw(account, amount):
    if amount > 0:
        account.withdraw(amount)
    else:
        print("Invalid withdrawal amount.")
