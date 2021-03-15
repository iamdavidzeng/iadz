# -*- coding: utf-8 -*-

import os
import sys

# 添加上级目录到当前文件的环境变量当中
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


if __name__ == "__main__":
    environ_lst = (
        os.path.dirname(__file__),
        os.path.join(os.path.dirname(__file__), ".."),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
    )
    for environ in environ_lst:
        print(environ)
