class Bank:
    def __init__(self,name):
        self.name = name
        self.balance = 100000000
        self.total_loan = 0
        self.bankrupt_status = False
        self.loan_status = True
        self.users = []
        self.account_type = ['current','savings']

    def set_balance(self,amount):
        self.balance += amount
        
    def find_account(self,bank,userID):
        for user in bank.users:
            if user.userID == userID:
                return user
        return None

    def balance_after_withdraw(self,amount):
        self.balance -= amount
    
    def add_loan(self,amount):
        self.total_loan += amount

