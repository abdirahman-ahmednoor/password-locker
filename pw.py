import random
import string 

class Credentials:
    """Class to generate credentials for different accounts.
    """
    accounts_list = []
    user_accounts = []
    def __init__(self, account_name, email, username, password, user):
        """__init__ method to help define the propertiesof our credentials objects.

        Args:
          account_name(string): New name of the credential account.
          email(string): New email address associated with that credentials.
          username(string):New username for that credential
          password(string):New password.
          user([string]): Current logged in user.
        """
        self.account_name = account_name
        self.email = email
        self.username = username
        self.password = password
        self.user = user


    def save_account(self):
        """self_account method saves credential objects into accounts_list
        """
        Credentials.accounts_list.append(self)

    @classmethod
    def generate_pw(cls, pw_length):
        """generate_pw method that generates random password.
        
        Agrs:
          pw_length (number): Length of generated password.

        Return:
           string: Return the generated password. 
        """
        pw= ''.join(random.choice(string.ascii_letter)for i in range(pw_length))
        return pw

    @classmethod
    def set_pw(cls, pw):
        """set_pw method that sets a given password.

        Args:
          pw (string): User password to be set.

        Returns:
          string: Password.
        """
        return pw

    @classmethod
    def dispaly_accounts(cls, pw):
        """"display_accounts taht loops through the accounts list and filters only those that belong to the current logged in user.

        Args:
          user (User): Current user.

        Returns: 
           Credentials: List of filtered credentials.
        """
        for account in cls.accounts_list:
            if account.user == User:
                cls.user_accounts.append(account)
        return cls.user_accounts

    def delete_account(self):
        """delete_account method taht removes a saved credential from the credentials list.
        """
        Credentials.accounts_list.remove(self)                           

class User:
    """Class to manage user accounts.
    """

    user_list = []
    def __init__(self, fname, lname, username, password):
        """__init__method to generate credentials objects.
        
        Args:
          fname (string): New user first name.
          lname (string): New user last name.
          username (string): New user usernmae.
          password (string): New user password.
        """
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password  

    def save_user(self):
        """save_user method taht saves user objects into the users list.
        """
        User.users_list.append(self)

    @classmethod
    def user_login(cls, username, pw):
        """user_login that handles user logging in.

        Args:
          username (string): Username to log in.
          pw (string): User password 

        Returns:
           User: Returns a user object that matches the given username and password.
           """
        for user in cls.user_list:
               if user.username == username and user.password == pw:
                   return user      
    
    def delete_user(self):
        """delete_user that removes a user from the list of ussers.
        """
        User.users_list.remove(self)

    
###test data ######

user1 = User('Abdirahman', 'Noor', 'test', 't3st')
User.user_list.append(user1)

account1 = Credentials('Twitter', 'abdirahman@mail.com', 'blade', 'fsdjHJKL', '')
account2 = Credentials('Facebook', 'abdirahman@mail.com', 'noor', 'svwGIKLO', '')

Credentials.accounts_list.append(account1)
Credentials.accounts_list.append(account2)