import unittest

from utils.encryption import *


class TestEncryption(unittest.TestCase):
    def test_encrypted_is_same_as_decrypted(self):
        """Test that an encrypted message can be decrypted."""
        message = "This is a test message."

        # Generate a keypair
        keypair = KeyPair()
        keypair.generate_key_pair()

        # Encrypt the message
        encryption_instance = Encryption(keypair)
        encrypted_data = encryption_instance.encrypt(message)

        # Decrypt the message and compare it to the original message
        self.assertEqual(
            encryption_instance.decrypt(encrypted_data).decode(),
            message,
        )

    def test_encrypted_is_not_same_as_original(self):
        """Test that an encrypted message is not the same as the original message."""
        message = "This is a test message."

        # Generate a keypair
        keypair = KeyPair()
        keypair.generate_key_pair()

        # Encrypt the message
        encryption_instance = Encryption(keypair)
        encrypted_data = encryption_instance.encrypt(message)

        # Compare the encrypted message to the original message
        self.assertNotEqual(
            encrypted_data,
            message.encode(),
        )


if __name__ == "__main__":
    unittest.main()
