import unittest

from validation import *

class TestPrivateKeyPasswordValidation(unittest.TestCase):
    def test_strong_password(self):
        self.assertTrue(check_valid_private_key_password("TestP@ssw0rd")[0])
        self.assertTrue(check_valid_private_key_password("1123Abcd123#")[0])
        self.assertTrue(check_valid_private_key_password("ALLl0werc@Ase1$")[0])

    def test_weak_password(self):
        self.assertFalse(check_valid_private_key_password("Test123!")[0])
        self.assertFalse(check_valid_private_key_password("mypassword")[0])
        self.assertFalse(check_valid_private_key_password("12345678")[0])

    def test_no_password(self):
        self.assertFalse(check_valid_private_key_password("")[0])
        self.assertFalse(check_valid_private_key_password(" ")[0])
        self.assertFalse(check_valid_private_key_password(None)[0])
    
    def test_password_length(self):
        self.assertEqual(check_valid_private_key_password("Abc123!")[1], "Password must be at least 12 characters long")
        self.assertEqual(check_valid_private_key_password("Abc123!Abc123!")[1], None)
    
    def test_password_digit(self):
        self.assertEqual(check_valid_private_key_password("Abcdefghijk!")[1], "Password must contain at least one digit")
        self.assertEqual(check_valid_private_key_password("ABCDEFGH1JK!")[1], "Password must contain at least one lowercase letter")
    
    def test_password_lowercase(self):
        self.assertEqual(check_valid_private_key_password("ABCDEFGH1JK!")[1], "Password must contain at least one lowercase letter")
        self.assertEqual(check_valid_private_key_password("abcdefgh1jk!")[1], "Password must contain at least one uppercase letter")

    def test_password_uppercase(self):
        self.assertEqual(check_valid_private_key_password("abcdefgh1jk!")[1], "Password must contain at least one uppercase letter")
        self.assertEqual(check_valid_private_key_password("Abcdefgh1jkl")[1], "Password must contain at least one special character")

    def test_password_special_character(self):
        self.assertEqual(check_valid_private_key_password("Abcdefgh1jkl")[1], "Password must contain at least one special character")
        self.assertEqual(check_valid_private_key_password("Abcdefgh1jk!")[1], None)


if __name__ == "__main__":
    unittest.main()