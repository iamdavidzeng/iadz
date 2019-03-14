#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import argparse


ACTION_CHOICES = ['count', 'fix']

def setup_parser():
    parser = argparse.ArgumentParser(
        "Make a test about use parser."
    )
    parser.add_argument(
        "--action",
        choices=ACTION_CHOICES,
        help="count the number of student or fix it."
    )
    parser.add_argument(
        "--limit",
        help="Number of records per pair."
    )
    return parser


if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args()

    if (not args.action) or (args.action not in ACTION_CHOICES):
        parser.print_help()
        sys.exit(2)
    elif args.action == ACTION_CHOICES[1]:
        print("Doing: Fix it by creating user.")
        if not args.limit:
            parser.print_help()
            limit = 10
        else:
            limit = int(args.limit)
    else:
        limit = 0
        print("Doing: Count the Number of users.")

    if args.action:
        print("Action: {}".format(args.action))
