# -*- coding: utf-8 -*-


def read_file(file_path):

    with open(file_path, "r") as file:

        return file.read()


def read_file_to_binary(path):

    with open(path, "rb") as key_file:

        return key_file.read()


if __name__ == "__main__":

    path = "/Users/a/.ssh/id_rsa"

    file_string = read_file(path)
    print(f"file_string: {file_string}")
