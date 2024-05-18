from user import User,Admin
from bank import Bank


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