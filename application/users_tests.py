#user testing module

from users import Users
from users import USERS
import unittest

class UserManagementTestcase(unittest.TestCase):

    def setUp(self):
        self.user = Users()
        self.current_user = USERS
        self.email = "jaykhaleesi@gmail.com"
        self.username = "jkahleesi"
        self.password = "321654987"


        def test_if_user_added(self):
            test_user = self.user.add_user(self.user_email, self.username, self.password)
            self.assertEqual(test_user, "User added successfully.")


