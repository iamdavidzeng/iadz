# -*- coding: utf-8 -*-
import random, string, base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def generate_private_key():
    return "".join(random.sample(string.ascii_letters + string.digits, 32))


def encrypt(secret_key, data):
    secret_key = secret_key.encode("utf-8")
    encryptor = AES.new(key=secret_key, mode=AES.MODE_CBC)
    cipher_text = encryptor.encrypt(pad(data.encode("utf-8"), AES.block_size))
    return base64.b64encode(cipher_text).decode("utf-8"), base64.b64encode(encryptor.iv).decode("utf-8")


def decrypt(secret_key, data, iv):
    secret_key = secret_key.encode("utf-8")
    iv = base64.b64decode(iv)
    decryptor = AES.new(key=secret_key, mode=AES.MODE_CBC, iv=iv)

    data = base64.b64decode(data)

    decrypted = decryptor.decrypt(data)

    return unpad(decrypted, AES.block_size).decode("utf-8")


if __name__ == "__main__":

    text = "gibbs@student.c3"

    secret_key = "Cs0n1jWi6PGVXqO4dElegAt8bBzx3yaU"
    print(f"private_key: {secret_key}")

    encrypted1, iv1 = encrypt(secret_key, "gibbs1@student.com")
    print(f"encrypted1: {encrypted1}, iv1: {iv1}")
    encrypted2, iv2 = encrypt(secret_key, "gibbs2@student.com")
    print(f"encrypted2: {encrypted2}, iv2: {iv2}")

    decrypted1 = decrypt(
        secret_key,
        encrypted1,
        iv1,
    )
    print(f"decrypted1: {decrypted1}")
    decrypted2 = decrypt(
        secret_key,
        encrypted2,
        iv2
    )
    print(f"decrypted2: {decrypted2}")
