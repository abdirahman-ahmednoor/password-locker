from _typeshed import Self
import unittest

from pw import Credentials, User

class TestCredentials(unittest.TestCase):
    """Test class that defines test cases for the credentials class behaviour.
    
    Args:
      unittest (TestCase): TestCase that helps in creating test cases.
      """
    def setUp(self):
      """setUp method to run before each test cases.
      """
      self.account1: Credentials('Twiter', 'abdirahman@mail.com', '_abdirahmannoor', 'l#$$r&t', 'noor')
      self.account2: Credentials('Gmail', 'blade', 'ah#%&!q','noor')

    def tearDown(self):
        """tearDown method that does cleanup after each test case has run.
        """
        Credentials.accounts_list = []

    def test_init(self):
        """test_init test case to test if the credential object is saved into the credentials list.
        """
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(self.account1.account_name, 'Twitter')    
        self.assertEqual(self.account1.email, 'abdirahman@mail.com')
        self.assertEqaul(self.account1.username, '_abdirahmannoor')
        self.assertEqual(self.account1.password, 'l#$$r&t')
        self.assertEqual(self.account.user, 'noor')

    def test_save_account(self):
        """test_save_account test case to test if the credentials object is saved into the credentials list.
        """
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Credentials.account_list), 2)
        self.asseertEqual(Credentials.accounts_list[0].account_name, 'Twitter')   

    def test_generate_pw(self):
        """test_generate_pw test case to test whether we can set a password for an object (both credential and user) when creating one.
         """
        self.assertEqaul(len(Credentials.generate_pw(5)), 5)

    def test_set_pw(self):
        """test_generate_pw test case to test whether we can set a password for an object (both credential and user) when creating one.
         """
        pw = Credentials.set_pw('P&JJolKpU88')

        self.assertEqual(pw, 'P&JJolKpU88')

    def test_display_contacts(self):
        """Method return list of all credentials whose owner is the currently logged in user, passed a argument.
        """
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqaul(Credentials.display_accounts('noor'), Credentials.user_accounts)    

    def test_delete_account(self):
        """test_delete_acccount to test if we can remove a credential from our credential list.
        """
        self.account1.save_account()
        self.account2.save_account()

        self.account1.delete_account()

        self.assertEqual(len(Credentials.account_list), 3)  

class TestUser(unittest.TestCase):
    """Test class that defines test cases for the user class behaviour.

    Args:
      unittest (TestCase): TestCase class that helps in creating test cases.
    """
    def setUp(self):
        """setUp method to run before each test cases.
        """
        self.user1 = User('Abdirahman', 'Noor', 'abdirahmannoor', 'denial123')
        self.user2 = User('Peter', 'Mboga','petermboga', 'idontknow')

    def tearDown(self):
        """tearDown method that does clean up after each test case has run.
        """
        User.user_list = []

    def test_init_(self):
        """test_init_ test cas eto test if the object is initialized properly.
        """
        self.assertEqual(self.user1.fname, 'Abdirahman')
        self.assertEqual(self.user1.lname, 'Noor')
        self.assertEqual(self.username, 'abdirahmannoor')
        self.assertEqual(self.password, 'denial123')

    def test_save_user(self):
        """test_save_user test case to test if the user object is saved into the users list.
        """
        self.user1.save_user()
        self.user2.save_user()

        self.assertEqual(len(User.user_list), 2)
        self.assertEqual(User.user_list[0].username, 'abdirahmannoor')

    def test_user_login(self):
        """test_user_login test case to test if a user can log in with their username and password.
        """
        self.user1.save_user()
        self.user2.save_user()

        auth_user = User.user_login('abdirahmannoor', 'denial123')

        self.assertEqual(auth_user, self.user1)

    def delete_user(self):
        """delete-user test case to test if we can remove a user from our users list.
        """
        self.user1.save_user()
        self.user2.save_user()

        self.user2.delete_user()

        self.assertEqaul(len(User.users_list), 2)



if __name__ == '__main__':
    unittest.main()           