# -*- coding: utf-8 -*-


import base64
import sys
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


assert sys.version_info >= (3, 4)


def load_private_key(private_key):

    return serialization.load_pem_private_key(
        private_key.encode("utf-8"), password=None, backend=default_backend()
    )


def load_public_key(publish_key):

    return serialization.load_ssh_public_key(
        data=publish_key.encode("utf-8"), backend=default_backend()
    )


def encrypt(data, publish_key):
    key = load_public_key(publish_key)

    ciphertext = key.encrypt(
        data.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None,
        ),
    )
    return base64.b64encode(ciphertext).decode("utf-8")


def decrypt(data, private_key):
    private_key = load_private_key(private_key)

    # Allow empty value
    if not data:
        return data

    # Handle list
    if isinstance(data, list):
        res = []
        for value in data:
            res.append(decrypt(value, private_key))
        return res

    # Handle dict
    if isinstance(data, dict):
        res = {}
        for key, value in data.items():
            res[key] = decrypt(value, private_key)
        return res

    if not isinstance(data, str):
        return data

    parts = data.replace(" ", "").replace("\r\n", "")

    base64_encrypted = parts

    decrypted = private_key.decrypt(
        base64.b64decode(base64_encrypted),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None,
        ),
    )
    return decrypted.decode("utf-8")


if __name__ == "__main__":

    name = "gibbs@student.com"

    publish_key = os.getenv("PUBLISH_KEY")

    private_key = os.getenv("PRIVATE_KEY")

    encrypted = encrypt(name, publish_key)
    print(f"encrypted: {encrypted}")

    decrypted = decrypt(encrypted, private_key)
    print(f"decrypted: {decrypted}")
