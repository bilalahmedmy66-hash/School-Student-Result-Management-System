# modules/calculations.py

"""
Calculation Module
School Student Result Management System

This module handles:
- Total marks
- Overall percentage
- Best 5 marks
- Best 5 percentage
- PASS / FAIL calculation
"""


# ============================================================
# TOTAL MARKS
# ============================================================

def calculate_total(marks):
    """
    Calculate total marks.

    Parameters:
        marks (dict):
            Example:
            {
                "English": 80,
                "Hindi": 75,
                "Mathematics": 90
            }

    Returns:
        int: Total marks
    """

    return sum(marks.values())


# ============================================================
# OVERALL PERCENTAGE
# ============================================================

def calculate_percentage(marks):
    """
    Calculate overall percentage based on all subjects.

    Every subject is assumed to have a maximum of 100 marks.
    """

    if not marks:
        return 0.0

    total_marks = calculate_total(marks)

    maximum_marks = len(marks) * 100

    percentage = (total_marks / maximum_marks) * 100

    return round(percentage, 2)


# ============================================================
# BEST 5 TOTAL
# ============================================================

def calculate_best_5_total(marks):
    """
    Sort all subject marks in descending order
    and select the highest five marks.

    If fewer than five subjects exist, all available
    marks are used.
    """

    sorted_marks = sorted(
        marks.values(),
        reverse=True
    )

    best_five = sorted_marks[:5]

    return sum(best_five)


# ============================================================
# BEST 5 PERCENTAGE
# ============================================================

def calculate_best_5_percentage(marks):
    """
    Calculate Best 5 Percentage.

    Five subjects = maximum 500 marks.

    Formula:

        Best 5 Total / 500 * 100

    If fewer than five subjects exist, the maximum marks
    are adjusted accordingly.
    """

    if not marks:
        return 0.0

    sorted_marks = sorted(
        marks.values(),
        reverse=True
    )

    best_five = sorted_marks[:5]

    best_five_total = sum(best_five)

    maximum_marks = len(best_five) * 100

    percentage = (
        best_five_total / maximum_marks
    ) * 100

    return round(percentage, 2)


# ============================================================
# PASS / FAIL
# ============================================================

def calculate_result(marks):
    """
    Student passes only if every subject has
    at least 33 marks.

    If even one subject is below 33,
    the student is FAIL.
    """

    if not marks:
        return "FAIL"

    for mark in marks.values():

        if mark < 33:
            return "FAIL"

    return "PASS"


# ============================================================
# COMPLETE RESULT
# ============================================================

def calculate_complete_result(marks):
    """
    Calculate all result-related values at once.

    Returns a dictionary containing:

    Total Marks
    Overall Percentage
    Best 5 Total
    Best 5 Percentage
    Result
    """

    total = calculate_total(marks)

    percentage = calculate_percentage(marks)

    best_5_total = calculate_best_5_total(marks)

    best_5_percentage = calculate_best_5_percentage(marks)

    result = calculate_result(marks)

    return {
        "Total Marks": total,
        "Overall Percentage": percentage,
        "Best 5 Total": best_5_total,
        "Best 5 Percentage": best_5_percentage,
        "Result": result
    }