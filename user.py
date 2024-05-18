from abc import ABC
from bank import Bank
from datetime import datetime
class Person(ABC):
    def __init__(self,name,email,address):
        self.name = name
        self.email = email
        self.address = address


class User(Person):
    def __init__(self, name, email, address,account_type,userID):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = 0
        self.userID = userID
        self.can_borrow_loan = 2
        self.tranasaction_history = []

    def deposite(self,bank,amount):
        if amount > 0:
            self.balance += amount
            details = f'Successfully deposited :{amount}'
            print(f'\n\n{details}')
            self.tranasaction_history.append(f'{details} ,Time :{datetime.now()}')
            bank.set_balance(amount)
    
    def withdraw(self,bank,amount):
        if bank.bankrupt_status == True:
            print('The bank is bankrupt!!!')
        else:
            if amount > self.balance:
                print('Withdrawal amount exceeded!!')
            else:
                self.balance -= amount
                bank.balance_after_withdraw(amount)
                print(f'Successfuly withdraw {amount}')
                details = f'withdrawn {amount} Time :{datetime.now()}'
                self.tranasaction_history.append(details)
    
    def transfer_amount(self,bank,user,amount):

        if amount > self.balance:
            print('You dont have enough money to transfer!!!')
            return 
        
        if user in bank.users:
            self.balance -= amount
            user.balance += amount
            print(f'successfully transferd {amount} to {user.name} ')
            details = f'transferd {amount} to {user.name} Time :  {datetime.now()}'
            details1 = f'Received {amount} from {self.name} Time :  {datetime.now()}'
            self.tranasaction_history.append(details)
            user.tranasaction_history.append(details1)
        else:
            print('Account does not exist!!')
    
    def cheeck_balance(self):
        print(f'Your current balance is : {self.balance}')

    def create_account(self,bank,user):
        bank.users.append(user)
        print('\nSuccessfully created an account..')
        print('----------Your account details---------')
        print(f'Account name :{user.name}')
        print(f'Account email :{user.email}')
        print(f'Address :{user.address}')
        print(f'Account type :{user.account_type}')
        print(f'User ID :{user.userID}')
    
    def view_account(self):
        print(f'Account name : {self.name}')
        print(f'Email : {self.email}')
        print(f'Address : {self.address}')
        print(f'Account type : {self.account_type}')
        print(f'User Id : {self.userID}')


    def borrow_loan(self,bank,amount):
        if self.can_borrow_loan == 0:
            print('You borrowed 2 times,can\'t borrow any!!')

        elif bank.loan_status == False:
            print('Cannot borrow loan from the bank right now!!')
            
        elif bank.bankrupt_status == True:
            print('The bank is bankrupt!!')

        else:
            if amount > bank.balance:
                print('can\'t borrow ,too much loan!!')
            else:
                self.balance += amount
                self.can_borrow_loan -= 1
                bank.balance_after_withdraw(amount)
                details = f'Borrowed {amount} from {bank.name} Time :{datetime.now()}'
                self.tranasaction_history.append(details)
                bank.add_loan(amount)
                print(f'You borrowed : {amount} from {bank.name}')

            
    def view_transaction_history(self):
        print('******Transcation History********')
        if len(self.tranasaction_history) == 0:
            print('Your transaction list is empty!!')
        else:
            for i in self.tranasaction_history:
                print(i)

class Admin(Person):
    password = 'admin'
    def __init__(self, name, email, address):
        super().__init__(name, email, address)



    def view_users(self,bank):
        print('##########Bank user list##########')
        for user in bank.users:
            print(f'User Name : {user.name}')
            print(f'User Email : {user.email}')
            print(f'User Address : {user.address}')
            print(f'User Account type : {user.account_type}')
            print(f'User UserID : {user.userID}')
            print('\n')
        print('####################################')

    def delete_account(self,bank,userID):
        flag = 0
        for user in bank.users:
            if userID == user.userID:
                bank.users.remove(user)
                flag = 1
                print('successfully deleted user..')
                break
        if flag == 0:
            print('user not found!!')

    def create_account(self,bank,user):
        bank.users.append(user)   
        print('\nSuccessfully created an account..')
        print('----------Your account details---------')
        print(f'Account name :{user.name}')
        print(f'Account email :{user.email}')
        print(f'Address :{user.address}')
        print(f'Account type :{user.account_type}')
        print(f'User ID :{user.userID}')

    def view_total_balance_of_bank(self,bank):
        print(f'Total available balance : {bank.balance}')

    def off_loan_feature(self,bank):
        bank.loan_status = False
    
    def on_loan_feature(self,bank):
        bank.loan_status = True

    def on_bankrupt(self,bank):
        bank.bankrupt_status = True

    def off_bankrupt(self,bank):
        bank.bankrupt_status = False

    def view_total_loan(self,bank):
        print(f'Total loan amount is : {bank.total_loan}')
