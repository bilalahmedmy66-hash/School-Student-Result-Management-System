# modules/statistics.py

"""
Statistics Module
School Student Result Management System

Provides:
- Total students
- Passed students
- Failed students
- Pass percentage
- Average Best 5 percentage
- Highest Best 5 percentage
- Lowest Best 5 percentage
"""

import pandas as pd


def calculate_statistics(dataframe):

    if dataframe is None or dataframe.empty:
        return {
            "Total Students": 0,
            "Passed Students": 0,
            "Failed Students": 0,
            "Pass Percentage": 0.0,
            "Average Best 5 Percentage": 0.0,
            "Highest Best 5 Percentage": 0.0,
            "Lowest Best 5 Percentage": 0.0
        }

    total_students = len(dataframe)

    passed_students = (
        dataframe["Result"]
        .astype(str)
        .str.upper()
        .eq("PASS")
        .sum()
    )

    failed_students = (
        dataframe["Result"]
        .astype(str)
        .str.upper()
        .eq("FAIL")
        .sum()
    )

    pass_percentage = (
        passed_students / total_students
    ) * 100

    best_5_percentage = pd.to_numeric(
        dataframe["Best 5 Percentage"],
        errors="coerce"
    )

    average_best_5 = best_5_percentage.mean()
    highest_best_5 = best_5_percentage.max()
    lowest_best_5 = best_5_percentage.min()

    return {
        "Total Students": total_students,
        "Passed Students": int(passed_students),
        "Failed Students": int(failed_students),
        "Pass Percentage": round(pass_percentage, 2),
        "Average Best 5 Percentage": round(average_best_5, 2),
        "Highest Best 5 Percentage": round(highest_best_5, 2),
        "Lowest Best 5 Percentage": round(lowest_best_5, 2)
    }