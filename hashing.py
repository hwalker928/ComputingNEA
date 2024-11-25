from Crypto.PublicKey import RSA
from typing import Self
import log
import os


class KeyPair:
    def __init__(self):
        log.debug("KeyPair object created")

        self.__public_key = None
        self.__private_key = None
        self.__private_key_password = ""

    def generate_private_key(self) -> RSA.RsaKey:
        log.debug("Generating private key")

        self.__private_key = RSA.generate(2048)

        return self.__private_key

    def generate_public_key(self) -> RSA.RsaKey:
        log.debug("Generating public key")

        # TODO: check if __private_key is None
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
        except Exception as e:
            # TODO: make this return an actual error instead of a bool
            return False

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
