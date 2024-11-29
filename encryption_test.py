import unittest

from encryption import *


class TestEncryption(unittest.TestCase):
    def test_encrypted_is_same_as_decrypted(self):
        """Test that an encrypted message can be decrypted."""
        message = "This is a test message."

        keypair = KeyPair()
        keypair.generate_key_pair()

        encryption_instance = Encryption(keypair)
        encrypted_data = encryption_instance.encrypt(message)

        self.assertEqual(
            encryption_instance.decrypt(encrypted_data).decode(),
            message,
        )

    def test_encrypted_is_not_same_as_original(self):
        """Test that an encrypted message is not the same as the original message."""
        message = "This is a test message."

        keypair = KeyPair()
        keypair.generate_key_pair()

        encryption_instance = Encryption(keypair)
        encrypted_data = encryption_instance.encrypt(message)

        self.assertNotEqual(
            encrypted_data,
            message.encode(),
        )


if __name__ == "__main__":
    unittest.main()
