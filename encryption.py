from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from typing import Self
import log
import os
from base64 import b64encode
from base64 import b64decode


class KeyPair:
    def __init__(self):
        log.debug("KeyPair object created")

        self.__public_key = None
        self.__private_key = None
        self.__private_key_password = ""

    def get_public_key_instance(self) -> RSA.RsaKey:
        log.debug("Getting public key instance")

        if self.__public_key is None:
            raise Exception("Public key does not exist")

        return self.__public_key

    def get_private_key_instance(self) -> RSA.RsaKey:
        log.debug("Getting private key instance")

        if self.__private_key is None:
            raise Exception("Private key does not exist")

        return self.__private_key

    def generate_private_key(self) -> RSA.RsaKey:
        log.debug("Generating private key")

        self.__private_key = RSA.generate(2048)

        return self.__private_key

    def generate_public_key(self) -> RSA.RsaKey:
        log.debug("Generating public key")

        if self.__private_key is None:
            raise Exception("Private key does not exist")

        self.__public_key = self.__private_key.publickey()

        return self.__public_key

    def generate_key_pair(self) -> Self:
        log.debug("Generating key pair")

        self.generate_private_key()
        self.generate_public_key()

        return self

    def set_private_key_password(self, passphrase: str) -> Self:
        log.debug("Setting private key password")

        # TODO: implement validation
        self.__private_key_password = passphrase

        return self

    def load_existing_key_pair(self, password: str) -> bool:
        log.debug("Loading existing key pair")

        try:
            with open("keys/private.key", "rb") as content_file:
                self.__private_key = RSA.import_key(
                    content_file.read(), passphrase=password
                )
            with open("keys/public.key", "rb") as content_file:
                self.__public_key = RSA.import_key(content_file.read())
        except ValueError:
            return False
        except Exception as e:
            raise e

        return True

    def save_keys_to_files(self) -> None:
        os.makedirs("keys", exist_ok=True)

        with open("keys/private.key", "wb") as content_file:
            log.debug("Saving private key to file")

            content_file.write(
                self.__private_key.exportKey(passphrase=self.__private_key_password)
            )
        with open("keys/public.key", "wb") as content_file:
            log.debug("Saving public key to file")

            content_file.write(self.__public_key.exportKey("OpenSSH"))


class Encryption:
    def __init__(self, key_pair: KeyPair):
        log.debug("Encryption object created")

        self.__public_key = key_pair.get_public_key_instance()
        self.__private_key = key_pair.get_private_key_instance()

    def encrypt(self, message: str | bytes) -> bytes:
        log.debug("Encrypting message")

        if self.__public_key is None:
            raise Exception("Public key does not exist")

        if type(message) == str:
            message = message.encode()

        cipher_rsa = PKCS1_OAEP.new(self.__public_key)

        return cipher_rsa.encrypt(message)

    def decrypt(self, message: bytes) -> bytes:
        log.debug("Decrypting message")

        if self.__private_key is None:
            raise Exception("Private key does not exist")

        cipher_rsa = PKCS1_OAEP.new(self.__private_key)

        return cipher_rsa.decrypt(message)

    def b_to_str(self, message: bytes) -> str:
        return b64encode(message).decode()
