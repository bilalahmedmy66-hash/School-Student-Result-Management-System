# modules/topper.py

"""
Topper Module
School Student Result Management System

Finds the student(s) with the highest
Best 5 Percentage.
"""

import pandas as pd


def find_topper(dataframe):
    """
    Find student(s) having the highest
    Best 5 Percentage.

    Returns:
        Pandas DataFrame containing topper(s)
    """

    if dataframe is None or dataframe.empty:
        return pd.DataFrame()

    dataframe = dataframe.copy()

    dataframe["Best 5 Percentage"] = pd.to_numeric(
        dataframe["Best 5 Percentage"],
        errors="coerce"
    )

    dataframe = dataframe.dropna(
        subset=["Best 5 Percentage"]
    )

    if dataframe.empty:
        return pd.DataFrame()

    highest_percentage = dataframe[
        "Best 5 Percentage"
    ].max()

    topper = dataframe[
        dataframe["Best 5 Percentage"]
        == highest_percentage
    ]

    return topper