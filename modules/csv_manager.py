# modules/csv_manager.py

"""
CSV Management Module
School Student Result Management System

Handles:
- Creating school_data folder
- Creating CSV files
- Loading CSV files
- Saving student records
- Adding records to existing CSV files
"""

import os
import pandas as pd

from config import DATA_FOLDER, generate_csv_filename


# ============================================================
# CREATE DATA FOLDER
# ============================================================

def create_data_folder():
    """
    Create the school_data folder if it doesn't exist.
    """

    if not os.path.exists(DATA_FOLDER):

        os.makedirs(DATA_FOLDER)

        print(
            f"Created data folder: {DATA_FOLDER}"
        )


# ============================================================
# GET CSV PATH
# ============================================================

def get_csv_path(
    academic_year,
    student_class,
    stream,
    section
):
    """
    Generate the complete CSV file path.
    """

    create_data_folder()

    filename = generate_csv_filename(
        academic_year,
        student_class,
        stream,
        section
    )

    return os.path.join(
        DATA_FOLDER,
        filename
    )


# ============================================================
# LOAD STUDENTS
# ============================================================

def load_students(
    academic_year,
    student_class,
    stream,
    section
):
    """
    Load students from the appropriate CSV file.

    If the file doesn't exist, return an empty DataFrame.
    """

    csv_path = get_csv_path(
        academic_year,
        student_class,
        stream,
        section
    )

    if os.path.exists(csv_path):

        try:

            dataframe = pd.read_csv(
                csv_path
            )

            return dataframe

        except pd.errors.EmptyDataError:

            return pd.DataFrame()

    return pd.DataFrame()


# ============================================================
# SAVE ALL STUDENTS
# ============================================================

def save_students(
    dataframe,
    academic_year,
    student_class,
    stream,
    section
):
    """
    Save a complete DataFrame to CSV.
    """

    csv_path = get_csv_path(
        academic_year,
        student_class,
        stream,
        section
    )

    dataframe.to_csv(
        csv_path,
        index=False
    )

    return csv_path


# ============================================================
# ADD ONE STUDENT
# ============================================================

def add_student_to_csv(
    student,
    academic_year,
    student_class,
    stream,
    section
):
    """
    Add one student record to the appropriate CSV file.
    """

    dataframe = load_students(
        academic_year,
        student_class,
        stream,
        section
    )

    new_student = pd.DataFrame(
        [student]
    )

    if dataframe.empty:

        dataframe = new_student

    else:

        dataframe = pd.concat(
            [
                dataframe,
                new_student
            ],
            ignore_index=True
        )

    csv_path = save_students(
        dataframe,
        academic_year,
        student_class,
        stream,
        section
    )

    return dataframe, csv_path