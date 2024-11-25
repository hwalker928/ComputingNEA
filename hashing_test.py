import unittest

from hashing import *


class TestHashing(unittest.TestCase):
    def test_hash_string(self):
        set_salt("test")
        hash_password("password")
        self.assertEqual(
            hash_password("password"),
            "a7574a42198b7d7eee2c037703a0b95558f195457908d6975e681e2055fd5eb9",
        )

    def test_check_password(self):
        set_salt("test")
        hashed_password = hash_password("password")
        self.assertTrue(check_password("password", hashed_password))
        self.assertFalse(check_password("password", "wrong_hashed_password"))
        self.assertFalse(check_password("wrong_password", hashed_password))


if __name__ == "__main__":
    unittest.main()
