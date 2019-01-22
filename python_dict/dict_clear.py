# -*- coding:utf-8 -*-


import argparse


METHOD_CHOICES = ['a', 'b']


def setup_parser():
    parser = argparse.ArgumentParser(
        'use to clear which method to use.'
    )
    parser.add_argument(
        '--method',
        choices=METHOD_CHOICES,
        help='choose a or b.'
    )
    return parser

# 实际改变了x的内存地址指向，原来的内存地址依旧是一个字典。
def clear_a():
    x = {}
    y = x
    x['key'] = 'value'
    print('y:', y)
    x = {}
    print('y:', y)

# 改变了内存地址的内容，所以x和y都会变空字典。
def clear_b():
    x = {}
    y = x
    x['key'] = 'value'
    print('y:', y)
    x.clear()
    print('y:', y)


if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args()

    if not args.method or args.method not in METHOD_CHOICES:
        parser.print_help()
    elif args.method == METHOD_CHOICES[0]:
        clear_a()
    else:
        clear_b()
