class Account:
    def __init__(self, account_no, account_balance):
        self.account_no = account_no
        self.account_balance = account_balance

    def credit(self, credit_amount):
        self.account_balance += credit_amount

    def debit(self, debit_amount):
        if debit_amount <= self.account_balance:
            self.account_balance -= debit_amount
            print("Debited Amount: {}, Current Balance is : {}".format(debit_amount, self.account_balance))
        else:
            print("Insufficient Funds")

    def __repr__(self):
        return "Account No: {}, Balance: {}".format(self.account_no, self.account_balance)


my_account = Account(9999, 5000)
print(my_account)
my_account.credit(4000)
print(my_account)
my_account.debit(12000)
print(my_account)
my_account.debit(3000)
print(my_account)
