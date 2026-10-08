# modules/export.py

"""
Export Module
School Student Result Management System

Exports the complete result dataframe
to a CSV result sheet.
"""

import os


EXPORT_FOLDER = "exports"


def create_export_folder():

    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)


def export_result_sheet(
    dataframe,
    academic_year,
    student_class,
    stream,
    section
):

    if dataframe is None or dataframe.empty:
        print(
            "No student data available to export."
        )
        return None

    create_export_folder()

    if stream:

        safe_stream = stream.replace(
            "/",
            "-"
        )

        filename = (
            f"Result_{academic_year}_"
            f"Class{student_class}_"
            f"{safe_stream}_"
            f"{section}.csv"
        )

    else:

        filename = (
            f"Result_{academic_year}_"
            f"Class{student_class}_"
            f"{section}.csv"
        )

    file_path = os.path.join(
        EXPORT_FOLDER,
        filename
    )

    dataframe.to_csv(
        file_path,
        index=False
    )

    print(
        f"Result sheet exported successfully:"
        f"\n{file_path}"
    )

    return file_path