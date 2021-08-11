from __future__ import annotations


class Strategy:
    def algorithm(self):
        raise NotImplementedError


class Sha256(Strategy):
    def algorithm(self):
        print("sha256")


class Sha128(Strategy):
    def algorithm(self):
        print("sha128")


class Context:
    def __init__(self) -> None:
        self.strategy = None

    def set_srategy(self, strategy: Strategy):
        self.strategy = strategy

    def algorithm(self):
        self.strategy.algorithm()


if __name__ == "__main__":

    sha128 = Sha128()
    sha256 = Sha256()

    context = Context()
    context.set_srategy(sha128)
    context.algorithm()

    context.set_srategy(sha256)
    context.algorithm()
