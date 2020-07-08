# -*- coding:utf-8 -*-


import numpy as np
import pandas as pd


def use_data_frames():
    """
    Try to use pandas.DataFrame.
    """

    df = pd.DataFrame(
        np.random.randn(6, 4),
        columns=[
            "num_bookings",
            "sum_commission",
            "supply_input_score",
            "num_sessions",
        ],
    )

    weight = [1, 10, 100, 50]

    property_score = []
    for i, row in df["num_bookings"].iteritems():
        property_score.append(
            (df["num_bookings"][i] * weight[0])
            + (df["sum_commission"][i] * weight[1])
            + (df["supply_input_score"][i] * weight[2])
            + (df["num_sessions"][i] * weight[3])
        )

    df["property_score"] = property_score

    print(df)


if __name__ == "__main__":
    use_data_frames()
