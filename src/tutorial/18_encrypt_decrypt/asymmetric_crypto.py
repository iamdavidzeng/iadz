# -*- coding: utf-8 -*-
import base64
import sys
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


assert sys.version_info >= (3, 4)

class CryptoManagement:
    def __init__(self, publish_key, private_key) -> None:
        self.publish_key = serialization.load_ssh_public_key(
            data=publish_key.encode("utf-8"), backend=default_backend()
        )
        self.private_key = serialization.load_pem_private_key(
            data=private_key.encode("utf-8"), password=None, backend=default_backend()
        )

    def encrypt(self, data):
        ciphertext = self.publish_key.encrypt(
            data.encode("utf-8"),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None,
            ),
        )
        return base64.b64encode(ciphertext).decode("utf-8")

    def decrypt(self, data):

        # Allow empty value
        if not data:
            return data

        # Handle list
        if isinstance(data, list):
            res = []
            for value in data:
                res.append(self.decrypt(value))
            return res

        # Handle dict
        if isinstance(data, dict):
            res = {}
            for key, value in data.items():
                res[key] = self.decrypt(value)
            return res

        if not isinstance(data, str):
            return data

        parts = data.replace(" ", "").replace("\r\n", "")

        base64_encrypted = parts

        decrypted = self.private_key.decrypt(
            base64.b64decode(base64_encrypted),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None,
            ),
        )
        return decrypted.decode("utf-8")


if __name__ == "__main__":

    data = "gibbs@student.com"

    publish_key = os.getenv("PUBLISH_KEY")

    private_key = os.getenv("PRIVATE_KEY")

    crypto = CryptoManagement(private_key=private_key, publish_key=publish_key)

    encrypted = crypto.encrypt(data)
    print(f"encrypted: {encrypted}")

    decrypted = crypto.decrypt(encrypted)
    print(f"decrypted: {decrypted}")
