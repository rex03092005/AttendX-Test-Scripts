# Updated login validation test script.

import unittest

def login(username, password):
    return username == "student" and password == "pass123"

class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        self.assertTrue(login("student", "pass123"))

    def test_invalid_password(self):
        self.assertFalse(login("student", "wrong"))

    def test_empty_username(self):
        self.assertFalse(login("", "pass123"))

if __name__ == "__main__":
    unittest.main()
