import unittest

from encryption import *


class TestEncryption(unittest.TestCase):
    def test_encrypted_is_same_as_decrypted(self):
        message = "This is a test message."

        keypair = KeyPair()
        keypair.generate_key_pair()

        encryption_instance = Encryption(keypair)
        encrypted_data = encryption_instance.encrypt(message)

        self.assertEqual(
            encryption_instance.decrypt(encrypted_data).decode(),
            message,
        )

    def test_encrypted_is_not_same_as_decrypted(self):
        message = "This is a test message."

        keypair = KeyPair()
        keypair.generate_key_pair()

        encryption_instance = Encryption(keypair)
        encrypted_data = encryption_instance.encrypt(message)

        self.assertNotEqual(
            encryption_instance.decrypt(encrypted_data).decode(),
            "This is not a test message.",
        )


if __name__ == "__main__":
    unittest.main()
