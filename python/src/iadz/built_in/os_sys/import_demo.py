# -*- coding: utf-8 -*-


def import_func(module_name):
    num = module_name.rfind(".")
    if num == -1:
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[num + 1 :]
        mod = __import__(module_name[:num], globals(), locals())
    for attr in dir(mod):
        if attr.startswith("_"):
            print("it's not what i want: %s" % attr)
            continue
        func = getattr(mod, attr)
        if callable(func):
            print("this's what i want: %s" % func.__name__)


if __name__ == "__main__":
    import_func("handles.py")
