from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from typing import Self
from utils import log
import os


class KeyPair:
    def __init__(self):
        log.debug("KeyPair object created")

        # Initialize the keys to None
        self.__public_key = None
        self.__private_key = None
        self.__private_key_password = ""

    def get_public_key_instance(self) -> RSA.RsaKey:
        log.debug("Getting public key instance")

        # Check if the public key exists
        if self.__public_key is None:
            raise Exception("Public key does not exist")

        return self.__public_key

    def get_private_key_instance(self) -> RSA.RsaKey:
        log.debug("Getting private key instance")

        # Check if the private key exists
        if self.__private_key is None:
            raise Exception("Private key does not exist")

        return self.__private_key

    def generate_private_key(self) -> RSA.RsaKey:
        log.debug("Generating private key")

        # Generate a new private key using RSA
        self.__private_key = RSA.generate(2048)

        return self.__private_key

    def generate_public_key(self) -> RSA.RsaKey:
        log.debug("Generating public key")

        # Check if the private key exists
        if self.__private_key is None:
            raise Exception("Private key does not exist")

        # Generate the public key from the private key
        self.__public_key = self.__private_key.publickey()

        return self.__public_key

    def generate_key_pair(self) -> Self:
        log.debug("Generating key pair")

        # Generate the private and public keys using the functions
        self.generate_private_key()
        self.generate_public_key()

        return self

    def set_private_key_password(self, passphrase: str) -> Self:
        log.debug("Setting private key password")

        self.__private_key_password = passphrase

        return self

    def save_keys_to_files(self) -> None:
        # Create the keys directory if it does not exist
        os.makedirs("keys", exist_ok=True)

        with open("keys/private.key", "wb") as content_file:
            log.debug("Saving private key to file")

            # Export the private key to a file with the password
            content_file.write(
                self.__private_key.exportKey(passphrase=self.__private_key_password)
            )
        with open("keys/public.key", "wb") as content_file:
            log.debug("Saving public key to file")

            # Export the public key to a file
            content_file.write(self.__public_key.exportKey("OpenSSH"))

    def load_existing_key_pair(self, password: str) -> bool:
        log.debug("Loading existing key pair")

        try:
            with open("keys/private.key", "rb") as key_file:
                self.__private_key = RSA.import_key(
                    key_file.read(), passphrase=password
                )
            with open("keys/public.key", "rb") as key_file:
                self.__public_key = RSA.import_key(key_file.read())
        except ValueError:
            # If the password is incorrect, the RSA.import_key function will raise a ValueError
            # In this case, we return False
            return False
        except Exception as e:
            # If any other exception occurs, we raise it
            raise e

        return True


class Encryption:
    def __init__(self, key_pair: KeyPair):
        log.debug("Encryption object created")

        # Get the public and private key instances from the key pair
        self.__public_key = key_pair.get_public_key_instance()
        self.__private_key = key_pair.get_private_key_instance()

    def encrypt(self, message: str | bytes) -> bytes:
        log.debug("Encrypting message")

        # Check if the public key exists
        if self.__public_key is None:
            raise Exception("Public key does not exist")

        # If the message is a string, encode it to bytes
        if type(message) == str:
            message = message.encode()

        # Create a new cipher using the public key
        cipher_rsa = PKCS1_OAEP.new(self.__public_key)

        # Return the encrypted message
        return cipher_rsa.encrypt(message)

    def decrypt(self, message: bytes) -> bytes:
        log.debug("Decrypting message")

        # Check if the private key exists
        if self.__private_key is None:
            raise Exception("Private key does not exist")

        # Create a new cipher using the private key
        cipher_rsa = PKCS1_OAEP.new(self.__private_key)

        # Return the decrypted message
        return cipher_rsa.decrypt(message)
