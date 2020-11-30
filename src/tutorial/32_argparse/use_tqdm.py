# -*- coding: utf-8 -*-

import argparse
from time import sleep

from tqdm import tqdm


def setup_parser():
    parser = argparse.ArgumentParser(
        description="Bash use to test tqdm"
    )
    parser.add_argument(
        "--num",
        help="Spcify the number of item to count",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--offset",
        help="Spcify the start position of items",
        type=int,
        default=0
    )
    parser.add_argument(
        "--limit",
        help="Limit the item for count",
        type=int,
        default=10000,
    )
    return parser


class Counter():

    def __init__(self, num, offset, limit):
        self.num = num
        self.offset = offset
        self.limit = limit

    def main(self):
        with tqdm(total=self.num, ncols=100) as pbar:
            for i in range(self.num):
                sleep(0.1)
                pbar.update(1)


if __name__ == "__main__":
    parser = setup_parser()
    args_ = parser.parse_args()
    Counter(args_.num, args_.offset, args_.limit).main()
    print("All done! ✨ 🍰 ✨")
