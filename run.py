#function
from pw import Credentials, User

def create_account(name, email, uname, pw, user):
    """Function to create a new contact.
    """
    new_credentials = Credentials(name, email, uname, pw, user)
    return new_credentials

def save_account(account):
        """Function to save a credentials.
        """
        account.save_account()

def generate_pw(length):
    """Function to generate a newe random password.
    """
    return Credentials.set_pw(length)

def set_pw(pw):
    """Function to set credential password.
    """
    return Credentials.set_pw(pw)

def display_accounts(user):
    """Function all returns all credentials of logged n user.
    """
    account = Credentials.display_accounts(user)
    return accounts

def delete_account(account):
    """Function to delete an account.
    """
    account.delete_account()

#user function
def create_user(fname, lname, uname, pw):
    """Function for creating new user.
    """
    new_user = User(name, lname, uname, pw)
    return new_user 

def save_user(user):
    """Function to save user.
    """
    user.save_user()

def user_login(uanme, pw):
    """Funtion to handle user login.
    """
    return User.user_login(uname, pw)

def delete_user(user):
    """Function to remove user.
    """
    user.delete_user()

#main function
def main():
    print("Hello. Welcome to PassLock. Please login and add new account to continue .\n\n")

    exit = False
    while not exit:
        print('what would you like to do? (enter number to delect)')
        print('--'*25)
        print('Create new user.\n2. Login in a exciting account.\n3. Remove user.\n4. Exit.')
        choice = input('Enter choice')

          #create new user       
        if choice == '1':
            print('\n\n***Create new user***\n')
            fname = input('First name: ')
            lname = input('Last name: ')
            username = input('Username: ')

            #choose mode of password
            while True:
                print('Password: \n\t1. Autogenerate password./n/t2. Enter custom password.')
                pw_input_choice = input('\tEnter choice: ')
                if pw_input_choice == '1':
                    pw_length = int(input('Enter desire autogenerated password length'))
                    password = generate_pw(pw_length)
                    break
                else:
                    print('Invalid choice. Try again.\n\n')    
                   
             save_user(create_user(fname, lname, username, password))
             print(f'\nNew user {fname} {lname} created.\n\n')
        
         elif choice == '2':
             print('\n\n***Log In***\n')
             uname = input('Enter username: ')
             pw = input('Enter password: ')
             user_logged_in = user_lgg