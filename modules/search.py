# modules/search.py

"""
Search Module
School Student Result Management System

Handles:
- Search by Roll Number
- Search by Student Name
- Case-insensitive searching
"""

import pandas as pd


def search_by_roll_number(dataframe, roll_number):
    """
    Search students by Roll Number.
    """

    if dataframe is None or dataframe.empty:
        return pd.DataFrame()

    roll_number = str(
        roll_number
    ).strip().lower()

    result = dataframe[
        dataframe["Roll Number"]
        .astype(str)
        .str.strip()
        .str.lower()
        == roll_number
    ]

    return result


def search_by_name(dataframe, name):
    """
    Search students by Student Name.

    Search is:
    - Case-insensitive
    - Partial-match supported
    """

    if dataframe is None or dataframe.empty:
        return pd.DataFrame()

    name = str(
        name
    ).strip().lower()

    result = dataframe[
        dataframe["Student Name"]
        .astype(str)
        .str.lower()
        .str.contains(
            name,
            na=False
        )
    ]

    return result


def search_students(
    dataframe,
    search_type,
    search_value
):
    """
    General search function.

    search_type:
        roll
        name
    """

    if search_type == "roll":

        return search_by_roll_number(
            dataframe,
            search_value
        )

    elif search_type == "name":

        return search_by_name(
            dataframe,
            search_value
        )

    return pd.DataFrame()