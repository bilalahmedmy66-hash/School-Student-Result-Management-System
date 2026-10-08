# config.py

"""
Configuration Module
School Student Result Management System
"""


# Folder configuration
DATA_FOLDER = "school_data"
EXPORT_FOLDER = "exports"
DATABASE_FOLDER = "database"


# Supported classes
SUPPORTED_CLASSES = [9, 10, 11, 12]


# Supported streams
STREAMS = [
    "Science",
    "Commerce",
    "Arts/Humanities"
]


# Supported sections
SECTIONS = [
    "A",
    "B",
    "C",
    "D"
]


def get_academic_year():
    """
    Ask the user to enter an academic year.

    Example:
    2026-27
    """

    while True:

        academic_year = input(
            "\nEnter Academic Year (example: 2026-27): "
        ).strip()

        if not academic_year:
            print("Academic Year cannot be blank.")
            continue

        # Basic format validation
        import re

        pattern = r"^\d{4}-\d{2}$"

        if not re.fullmatch(pattern, academic_year):
            print(
                "Invalid Academic Year format."
                "\nPlease use format YYYY-YY."
                "\nExample: 2026-27"
            )
            continue

        return academic_year


def get_section():
    """
    Ask the user to select a section.
    """

    while True:

        print("\n========== SECTION SELECTION ==========")

        for index, section in enumerate(SECTIONS, start=1):
            print(f"{index}. Section {section}")

        choice = input(
            f"Enter your choice (1-{len(SECTIONS)}): "
        ).strip()

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(SECTIONS):
            return SECTIONS[choice - 1]

        print(
            f"Invalid choice. Please select 1-{len(SECTIONS)}."
        )


def generate_csv_filename(
    academic_year,
    student_class,
    stream,
    section
):
    """
    Generate the CSV filename based on:

    Academic Year
    Class
    Stream
    Section
    """

    # Classes 9 and 10 don't have streams
    if student_class in [9, 10]:

        filename = (
            f"{academic_year}_"
            f"Class{student_class}_"
            f"{section}.csv"
        )

    else:

        # Remove slash from Arts/Humanities
        safe_stream = stream.replace("/", "-")

        filename = (
            f"{academic_year}_"
            f"Class{student_class}_"
            f"{safe_stream}_"
            f"{section}.csv"
        )

    return filename