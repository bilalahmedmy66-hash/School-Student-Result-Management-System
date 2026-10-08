# modules/validation.py

"""
Validation Module
School Student Result Management System

Handles validation of:
- Student names
- Roll numbers
- Marks
- General user input
"""

import re


# ============================================================
# NAME VALIDATION
# ============================================================

def validate_name(name):
    """
    Validate student name.

    Rules:
    - Cannot be blank
    - Only letters and spaces
    """

    name = name.strip()

    if not name:
        return False, "Student name cannot be blank."

    pattern = r"^[A-Za-z ]+$"

    if not re.fullmatch(pattern, name):
        return False, (
            "Student name can contain only "
            "letters and spaces."
        )

    return True, name


# ============================================================
# ROLL NUMBER VALIDATION
# ============================================================

def validate_roll_number(roll_number):
    """
    Validate roll number.

    Rules:
    - Cannot be blank
    - Must contain letters/numbers
    - Spaces are not allowed
    """

    roll_number = roll_number.strip()

    if not roll_number:
        return False, "Roll number cannot be blank."

    pattern = r"^[A-Za-z0-9]+$"

    if not re.fullmatch(pattern, roll_number):
        return False, (
            "Roll number can contain only "
            "letters and numbers."
        )

    return True, roll_number


# ============================================================
# MARK VALIDATION
# ============================================================

def validate_marks(mark):
    """
    Validate marks.

    Rules:
    - Must be numeric
    - Must be between 0 and 100
    """

    mark = mark.strip()

    if not mark:
        return False, "Marks cannot be blank."

    if not mark.isdigit():
        return False, "Marks must be a whole number."

    mark = int(mark)

    if mark < 0 or mark > 100:
        return False, "Marks must be between 0 and 100."

    return True, mark