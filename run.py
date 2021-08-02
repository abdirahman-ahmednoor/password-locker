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


def create_user(fname, Iname, uname, pw):
    """Function for creating new user.
    """
    new_user = User(name, Iname, uname, pw)
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


def main():
    print("Hello. Welcome to PassLock. Please login and add new account to continue ./n/n")