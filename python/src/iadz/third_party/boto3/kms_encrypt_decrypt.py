# -*- coding: utf-8 -*-

from base64 import encode
import os
import json
import base64

import boto3


AWS_REGION = "eu-west-1"


class KMSManager:
    def __init__(self, **kwargs):
        self.aws_access_key_id = kwargs["aws_access_key_id"]
        self.aws_secret_access_key = kwargs["aws_secret_access_key"]

    def setup(self):
        kms = boto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=AWS_REGION,
        ).client("kms")
        self.kms = kms

    def encrypt(self, data):
        ciphertext = self.kms.encrypt(
            KeyId="arn:aws:kms:eu-west-1:019838852892:key/cedf5aff-7290-4dbb-bfa5-3f9e8e50884d",
            Plaintext=json.dumps(data),
        )
        encoded_ciphertext = base64.b64encode(ciphertext["CiphertextBlob"])
        return encoded_ciphertext.decode("utf-8")

    def decrypt(self, data):
        decoded_ciphertext = base64.b64decode(data.encode("utf-8"))
        plaintext = self.kms.decrypt(CiphertextBlob=bytes(decoded_ciphertext))["Plaintext"]
        return json.loads(plaintext.decode("utf-8"))


if __name__ == "__main__":

    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    manager = KMSManager(
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key
    )
    manager.setup()

    encrypt_data = manager.encrypt("iamdavidzeng")
    print(f"encrypt_data: {encrypt_data}")

    decrypt_data = manager.decrypt(encrypt_data)
    print(f"decrypt_data: {decrypt_data} {type(decrypt_data)}")

