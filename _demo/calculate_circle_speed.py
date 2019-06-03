# -*- coding: utf-8 -*-


from datetime import datetime


def one_circle():

    is_from = False

    start = datetime.utcnow()

    for i in range(20):

        is_from = True

        a = True

    end = datetime.utcnow()

    interval = end - start

    return interval


def two_circle():

    if_from = False

    start = datetime.utcnow()

    for i in range(20):

        if i == 19:
            is_from = True
            break

    for i in range(20):

        a = True

    end = datetime.utcnow()

    interval = end - start

    return interval


if __name__ == "__main__":

    interval_1 = two_circle()

    interval_2 = one_circle()

    print(
        "interval_1: %s" % interval_1,
        "interval_2: %s" % interval_2, 
    )
