import unittest
from database.database_executor import DatabaseExecutor, DatabaseSession
from model.user_account import UserAccount


class TestDatabaseExecutor(unittest.TestCase):
    def setUp(self):
        self.db_exec: DatabaseExecutor = DatabaseExecutor()

    def test_get_all_user_accounts(self):
        user_accounts = self.db_exec.get_user_accounts()
        self.assertIsNotNone(user_accounts, "User accounts was empty")
        user_account = user_accounts[0]
        self.assertEqual('Bob', user_account.lastName, "Expected the users last name to be Bob")

    def test_add_delete_user_account(self):
        nu = UserAccount(firstName="Test", lastName="User")
        nu.save()

        user_accounts = self.db_exec.get_user_accounts()
        user_last_names = [u.lastName for u in user_accounts]
        self.assertIn("User", user_last_names, "New user not found in database")
        nu.delete()
        user_accounts = self.db_exec.get_user_accounts()
        user_last_names = [u.lastName for u in user_accounts]
        self.assertNotIn("User", user_last_names, "New user found in database")


if __name__ == '__main__':
    unittest.main()
