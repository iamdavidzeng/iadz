"""
Dependency Inversion Principle
"""

# Break
class XMLHttpService:
    def request(self, url: str, options: dict):
        pass


class Http:
    def __init__(self, xts: XMLHttpService) -> None:
        self.xts = XMLHttpService

    def get(self, url: str, optoins: dict):
        self.xts.request(url, "GET")

    def post(self, url: str, options: dict):
        self.xts.request(url, "POST")


# DIP
class Connection:
    def request(self, url: str, options: dict):
        pass


class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection

    def get(self, url: str, options: dict):
        self.http_connection.request(url, "GET")

    def post(self, url, options: dict):
        self.http_connection.request(url, "POST")


class XMLHttpService(Connection):
    xhr = None

    def request(self, url: str, options: dict):
        self.xhr.open()
        self.xhr.send()


class NodeHttpService(Connection):
    def request(self, url: str, options: dict):
        pass


class MockHttpService(Connection):
    def request(self, url: str, options: dict):
        pass