from abc import ABC
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

##bank part
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

##interfacing part

bank = Bank('Islami Bank Limitd')

def Customer_interface():

    while True:
        print(f'\n\n**********Welcome**************')
        print('1.Create account.')
        print('2.Deposite into your account.')
        print('3.Withdraw from your account.')
        print('4.Cheeck available balance.')
        print('5.Cheeck transaction history.')
        print('6.Take loan from bank.')
        print('7.Transfer amount.')
        print('8.Exit')
        choice = int(input('Enter your choice : '))
        print('\n')

        if choice == 1:
            name = input('Enter your account name : ')
            email = input('Enter your email : ')
            address = input('Enter your address :')
            account_type = input('Enter account type (account type should be either current or savings): ')
            if account_type.lower() not in bank.account_type:
                while True:
                    print('Invalid account type!!')
                    account_type = input('Enter account type (account type should be either current or savings): ')
                    if account_type.lower() == 'current' or account_type.lower() == 'savings':
                        break


            userid = f'xcc{name}{len(bank.users) + 101}'
            user = User(name,email,address,account_type,userid)
            user.create_account(bank,user)
        
        elif choice == 2:
            userID = input('Enter userID ,provided during creating your account : ')
            user = bank.find_account(bank,userID)

            if user:
                amount = int(input('Enter amount to be deposited : '))
                user.deposite(bank,amount)
            else:
                print('Account doesn\'t exist!!')

        elif choice == 3:
            userID = input('Enter userID ,provided during creating your account : ')
            user = bank.find_account(bank,userID)

            if user:
                amount = int(input('Enter amount to be withdraw : '))
                user.withdraw(bank,amount)
            else:
                print('Account doesn\'t exist!!')
        
        elif choice == 4:
            userID = input('Enter userID ,provided during creating your account : ')
            user = bank.find_account(bank,userID)

            if user:
                user.cheeck_balance()
            else:
                print('Account doesn\'t exist!!')

        elif choice == 5:
            userID = input('Enter userID ,provided during creating your account : ')
            user = bank.find_account(bank,userID)

            if user:
                user.view_transaction_history()
            else:
                print('Account doesn\'t exist!!')
        
        elif choice == 6:
            userID = input('Enter userID ,provided during creating your account : ')
            user = bank.find_account(bank,userID)

            if user:
                amount = int(input('Enter amount of loan to be borrowed : '))
                user.borrow_loan(bank,amount)
            else:
                print('Account doesn\'t exist!!')
        
        elif choice == 7:
            userID = input('Enter userID ,provided during creating your account : ')
            user = bank.find_account(bank,userID)

            if user:
                amount = int(input('Enter amount to transferd : '))
                userID = input('Enter userID where balance should be transferd : ')

                user2 =bank.find_account(bank,userID)

                if user2:
                    user.transfer_amount(bank,user2,amount)
                else:
                    print('cannot transfer , Transfer account does\'t exist !!')
            else:
                print('Account doesn\'t exist!!')
        
        elif choice == 8:
            print('Successfully existed as user!!\n')
            break
        else:
            print('Invalid choice!!!')

def Admin_interface():
    ad_name = input('Enter your name : ')
    email = input('Enter your email : ')
    address = input('Enter your address : ')
    password = input('Enter Admin panel\'s password : ')

    admin = Admin(ad_name,email,address)
    if admin.password !=  password:
        print('password is incorrect, cannot log in as admin !!!!!!')
    else:
        while True:
            print(f'\n__________Welcome Admin {admin.name}____________')
            print('1.Create an account.')
            print('2.delete an account.')
            print('3.See all user account list.')
            print('4.See total balance of bank.')
            print('5.See total loan amount.')
            print('6.On or Off loan feature.')
            print('7.On or Off bankrupt status.')
            print('8.Exit.')
            choice = int(input('Enter your choice: '))
        
            if choice == 1:
                name = input('Enter your account name : ')
                email = input('Enter your email : ')
                address = input('Enter your address :')
                account_type = input('Enter account type (account type should be either current or savings): ')

                if account_type.lower() not in bank.account_type:
                    while True:
                        print('Invalid account type!!')
                        account_type = input('Enter account type (account type should be either current or savings): ')
                        if account_type.lower() == 'current' or account_type.lower() == 'savings':
                            break

                userid = f'xcc{name}{len(bank.users) + 101}'
                user = User(name,email,address,account_type,userid)
                admin.create_account(bank,user)

            elif choice == 2:
                userID = input('Enter userID : ')
                user = bank.find_account(bank,userID)

                if user:
                    admin.delete_account(bank,userID)
                else:
                    print('Account doesn\'t exist!!')
        
            elif choice == 3:
                if len(bank.users) != 0:
                    admin.view_users(bank)
                else:
                    print('Users list is empty!!')

            elif choice == 4:
                admin.view_total_balance_of_bank(bank)
        
            elif choice == 5:
                admin.view_total_loan(bank)

            elif choice == 6:
                print('1.Press 1 to ON loan featrue.')
                print('2.Press 2 to OFF loan featrue.')
                choice = int(input('Enter your choice : '))

                if choice == 1:
                    admin.on_loan_feature(bank)
                elif choice == 2:
                    admin.off_loan_feature(bank)
                else:
                    print('Wrong key pressed!!')


            elif choice == 7:
                print('1.Press 1 to ON bankrupt status.')
                print('2.Press 2 to OFF bankrupt status.')
                choice = int(input('Enter your choice : '))

                if choice == 1:
                    admin.on_bankrupt(bank)
                elif choice == 2:
                    admin.off_bankrupt(bank)
                else:
                    print('Wrong key pressed!!')
            elif choice == 8:
                print('Successfully exited as admin..\n')
                break
            else:
                print('Invalid choice...!!!')


while True:
    print(f'**********welcome to {bank.name}************')
    print('1.Log in as User.')
    print('2.Log in as Admin.')
    print('3.Exit.')
    choice = int(input('Enter your choice : '))

    if choice == 1:
        Customer_interface()
    elif choice == 2:
        Admin_interface()
    elif choice == 3:
        print('Successfully exited the system...\n')
        break
    else:
        print('Invalid choice..!')
