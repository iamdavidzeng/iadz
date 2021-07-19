class BaseClient:
    def get_properties(self, *args, **kwargs):
        raise NotImplementedError


class SSClient(BaseClient):
    def __init__(self) -> None:
        super().__init__()


ss = SSClient()
ss.get_properties()
