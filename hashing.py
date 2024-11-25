from Crypto.PublicKey import RSA
from typing import Self


class KeyPair:
    def __init__(self):
        self.__public_key = None
        self.__private_key = None
        self.__private_key_password = ""

    def generate_private_key(self) -> RSA.RsaKey:
        self.__private_key = RSA.generate(2048)

        return self.__private_key

    def generate_public_key(self) -> RSA.RsaKey:
        # TODO: check if __key is None
        self.__public_key = self.__key.publickey()

        return self.__public_key

    def generate_key_pair(self) -> Self:
        self.generate_private_key()
        self.generate_public_key()

        return self

    def set_private_key_password(self, passphrase: str) -> Self:
        # TODO: implement validation
        self.__private_key_password = passphrase

        return self

    def save_keys_to_files(self):
        with open("keys/private.key", "wb") as content_file:
            content_file.write(
                self.__private_key.exportKey(passphrase=self.__private_key_password)
            )
        with open("keys/public.key", "wb") as content_file:
            content_file.write(self.__public_key.exportKey("OpenSSH"))


kp = KeyPair().generate_key_pair()
kp.save_keys_to_files()
