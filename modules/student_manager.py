# modules/student_manager.py

"""
Student Management Module

Handles:
- Student name
- Roll number
- Subject marks
- Duplicate roll number checking
- Result calculations
- Student record creation
"""

from modules.validation import (
    validate_name,
    validate_roll_number,
    validate_marks
)

from modules.calculations import (
    calculate_complete_result
)


# ============================================================
# GET EXISTING ROLL NUMBERS
# ============================================================

def get_existing_roll_numbers(dataframe):
    """
    Extract existing roll numbers from a Pandas DataFrame.

    Returns:
        set
    """

    if dataframe is None or dataframe.empty:
        return set()

    return set(
        dataframe["Roll Number"]
        .astype(str)
        .str.strip()
    )


# ============================================================
# STUDENT NAME
# ============================================================

def get_student_name():

    while True:

        name = input(
            "Enter Student Name: "
        ).strip()

        valid, result = validate_name(name)

        if valid:
            return result

        print(
            f"Invalid Name: {result}"
        )


# ============================================================
# ROLL NUMBER
# ============================================================

def get_roll_number(existing_roll_numbers=None):

    if existing_roll_numbers is None:
        existing_roll_numbers = set()

    while True:

        roll_number = input(
            "Enter Roll Number: "
        ).strip()

        valid, result = validate_roll_number(
            roll_number
        )

        if not valid:

            print(
                f"Invalid Roll Number: {result}"
            )

            continue

        # Convert to string for comparison
        roll_number = str(result)

        # Duplicate check
        if roll_number in existing_roll_numbers:

            print(
                "\nERROR: This Roll Number already exists."
            )

            print(
                "Please enter a different Roll Number.\n"
            )

            continue

        return roll_number


# ============================================================
# SUBJECT MARKS
# ============================================================

def get_subject_marks(subjects):

    marks = {}

    print("\n========== ENTER MARKS ==========")

    for subject in subjects:

        while True:

            mark = input(
                f"Enter marks for "
                f"{subject} (0-100): "
            ).strip()

            valid, result = validate_marks(mark)

            if valid:

                marks[subject] = result

                break

            print(
                f"Invalid Marks: {result}"
            )

    return marks


# ============================================================
# CREATE STUDENT RECORD
# ============================================================

def create_student_record(
    subjects,
    existing_roll_numbers=None
):
    """
    Create one complete student record.
    """

    print("\n======================================")
    print(" ENTER STUDENT DETAILS")
    print("======================================")

    roll_number = get_roll_number(
        existing_roll_numbers
    )

    name = get_student_name()

    marks = get_subject_marks(
        subjects
    )

    # Calculate result
    result_data = calculate_complete_result(
        marks
    )

    # Basic student information
    student = {
        "Roll Number": roll_number,
        "Student Name": name
    }

    # Add subject marks
    for subject in subjects:

        student[subject] = marks[subject]

    # Add calculated result information
    student.update(
        result_data
    )

    return student