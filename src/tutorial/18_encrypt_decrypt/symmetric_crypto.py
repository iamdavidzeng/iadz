# -*- coding: utf-8 -*-
import random, string, base64

from Crypto.Cipher import AES


def generate_private_key():
    return "".join(random.sample(string.ascii_letters + string.digits, 32))


class CryptoManagement:
    def __init__(self, private_key):
        self.private_key = private_key.encode("utf-8")

    def setup(self):
        """"
        A cipher object is stateful: once you have decrypted a message
        you cannot decrypt (or encrypt) another message with the same
        object.
        """
        self.encryptor = AES.new(
            key=self.private_key, mode=AES.MODE_CBC, iv=self.private_key[:16]
        )
        self.decryptor = AES.new(
            key=self.private_key, mode=AES.MODE_CBC, iv=self.private_key[:16]
        )

    def encrypt(self, data):
        cipher_text = self.encryptor.encrypt(self._padding(data).encode("utf-8"))
        return base64.b64encode(cipher_text).decode("utf-8")

    def decrypt(self, data):
        data = base64.b64decode(data)

        decrypted = self.decryptor.decrypt(data).decode("utf-8")

        return self._unpadding(decrypted)

    @staticmethod
    def _padding(data):
        padding_len = 16 - (len(data.encode("utf-8")) % 16)
        data += chr(padding_len) * padding_len
        return data

    @staticmethod
    def _unpadding(data):
        paidding_len = len(data)
        if paidding_len == 0:
            return data
        asc = ord(data[-1])
        print(asc)
        if asc >= 16:
            return data
        return data[:-asc]


if __name__ == "__main__":

    text = "gibbs@student.c3"

    private_key = generate_private_key()
    print(f"private_key: {private_key}")

    crypto = CryptoManagement(private_key=private_key)
    crypto.setup()

    encrypted = crypto.encrypt(text)
    print(f"encrypted: {encrypted}")

    decrypted = crypto.decrypt(encrypted)
    print(f"decrypted: {decrypted}")
