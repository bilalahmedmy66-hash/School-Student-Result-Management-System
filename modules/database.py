import os
import json
import sqlite3
import pandas as pd

from config import DATABASE_FOLDER


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

DATABASE_FILE = os.path.join(
    DATABASE_FOLDER,
    "school.db"
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    """
    Create and return a SQLite database connection.
    """

    os.makedirs(
        DATABASE_FOLDER,
        exist_ok=True
    )

    connection = sqlite3.connect(
        DATABASE_FILE
    )

    return connection


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def initialize_database():
    """
    Create the students table if it does not already exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            academic_year TEXT NOT NULL,

            student_class INTEGER NOT NULL,

            stream TEXT,

            section TEXT NOT NULL,

            roll_number TEXT NOT NULL,

            student_name TEXT NOT NULL,

            subjects TEXT NOT NULL,

            marks TEXT NOT NULL,

            total_marks INTEGER NOT NULL,

            overall_percentage REAL NOT NULL,

            best_5_total INTEGER NOT NULL,

            best_5_percentage REAL NOT NULL,

            result TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(
                academic_year,
                student_class,
                stream,
                section,
                roll_number
            )
        )
        """
    )

    connection.commit()
    connection.close()


# ============================================================
# INSERT STUDENT
# ============================================================

def insert_student(
    academic_year,
    student_class,
    stream,
    section,
    roll_number,
    student_name,
    subjects,
    marks,
    total_marks,
    overall_percentage,
    best_5_total,
    best_5_percentage,
    result
):
    """
    Insert one student record into SQLite.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO students (
                academic_year,
                student_class,
                stream,
                section,
                roll_number,
                student_name,
                subjects,
                marks,
                total_marks,
                overall_percentage,
                best_5_total,
                best_5_percentage,
                result
            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,

            (
                academic_year,
                student_class,
                stream,
                section,
                str(roll_number),
                student_name,
                json.dumps(subjects),
                json.dumps(marks),
                int(total_marks),
                float(overall_percentage),
                int(best_5_total),
                float(best_5_percentage),
                result
            )
        )

        connection.commit()

        return True

    except sqlite3.IntegrityError:

        connection.rollback()

        return False

    except Exception:

        connection.rollback()

        return False

    finally:

        connection.close()


# ============================================================
# INSERT STUDENT RECORD FROM DICTIONARY
# ============================================================

def insert_student_record(
    academic_year,
    student_class,
    stream,
    section,
    student
):
    """
    Insert a complete student dictionary into SQLite.
    """

    excluded_columns = {
        "Roll Number",
        "Student Name",
        "Total Marks",
        "Overall Percentage",
        "Best 5 Total",
        "Best 5 Percentage",
        "Result"
    }

    subjects = []
    marks = {}

    for key, value in student.items():

        if key not in excluded_columns:

            subjects.append(key)

            marks[key] = value

    return insert_student(

        academic_year=academic_year,

        student_class=student_class,

        stream=stream,

        section=section,

        roll_number=student["Roll Number"],

        student_name=student["Student Name"],

        subjects=subjects,

        marks=marks,

        total_marks=student["Total Marks"],

        overall_percentage=student["Overall Percentage"],

        best_5_total=student["Best 5 Total"],

        best_5_percentage=student["Best 5 Percentage"],

        result=student["Result"]
    )


# ============================================================
# GET ALL RAW STUDENTS
# ============================================================

def get_all_students(
    academic_year=None,
    student_class=None,
    stream=None,
    section=None
):
    """
    Return raw SQLite student records.
    """

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        SELECT *
        FROM students
        WHERE 1 = 1
    """

    parameters = []

    if academic_year is not None:

        query += """
            AND academic_year = ?
        """

        parameters.append(
            academic_year
        )

    if student_class is not None:

        query += """
            AND student_class = ?
        """

        parameters.append(
            student_class
        )

    if stream is None:

        query += """
            AND stream IS NULL
        """

    else:

        query += """
            AND stream = ?
        """

        parameters.append(
            stream
        )

    if section is not None:

        query += """
            AND section = ?
        """

        parameters.append(
            section
        )

    query += """
        ORDER BY CAST(roll_number AS INTEGER), roll_number
    """

    cursor.execute(
        query,
        parameters
    )

    rows = cursor.fetchall()

    connection.close()

    return rows


# ============================================================
# GET STUDENTS AS PANDAS DATAFRAME
# ============================================================

def get_students_dataframe(
    academic_year,
    student_class,
    stream,
    section
):
    """
    Read students from SQLite and return a Pandas DataFrame.
    """

    connection = get_connection()

    cursor = connection.cursor()

    if stream is None:

        cursor.execute(
            """
            SELECT
                roll_number,
                student_name,
                subjects,
                marks,
                total_marks,
                overall_percentage,
                best_5_total,
                best_5_percentage,
                result

            FROM students

            WHERE academic_year = ?

            AND student_class = ?

            AND stream IS NULL

            AND section = ?

            ORDER BY
                CAST(roll_number AS INTEGER),
                roll_number
            """,

            (
                academic_year,
                student_class,
                section
            )
        )

    else:

        cursor.execute(
            """
            SELECT
                roll_number,
                student_name,
                subjects,
                marks,
                total_marks,
                overall_percentage,
                best_5_total,
                best_5_percentage,
                result

            FROM students

            WHERE academic_year = ?

            AND student_class = ?

            AND stream = ?

            AND section = ?

            ORDER BY
                CAST(roll_number AS INTEGER),
                roll_number
            """,

            (
                academic_year,
                student_class,
                stream,
                section
            )
        )

    rows = cursor.fetchall()

    connection.close()

    records = []

    for row in rows:

        (
            roll_number,
            student_name,
            subjects_json,
            marks_json,
            total_marks,
            overall_percentage,
            best_5_total,
            best_5_percentage,
            result
        ) = row

        try:

            subjects = json.loads(
                subjects_json
            )

        except Exception:

            subjects = []

        try:

            marks = json.loads(
                marks_json
            )

        except Exception:

            marks = {}

        student = {

            "Roll Number": roll_number,

            "Student Name": student_name
        }

        for subject in subjects:

            student[subject] = marks.get(
                subject,
                0
            )

        student["Total Marks"] = total_marks

        student["Overall Percentage"] = overall_percentage

        student["Best 5 Total"] = best_5_total

        student["Best 5 Percentage"] = best_5_percentage

        student["Result"] = result

        records.append(
            student
        )

    if not records:

        return pd.DataFrame()

    return pd.DataFrame(
        records
    )


# ============================================================
# COUNT STUDENTS
# ============================================================

def count_students():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM students
        """
    )

    count = cursor.fetchone()[0]

    connection.close()

    return count


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student(
    academic_year,
    student_class,
    stream,
    section,
    old_roll_number,
    student
):
    """
    Update an existing student record in SQLite.
    """

    excluded_columns = {
        "Roll Number",
        "Student Name",
        "Total Marks",
        "Overall Percentage",
        "Best 5 Total",
        "Best 5 Percentage",
        "Result"
    }

    subjects = []

    marks = {}

    for key, value in student.items():

        if key not in excluded_columns:

            subjects.append(key)

            marks[key] = value

    connection = get_connection()

    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            UPDATE students

            SET

                roll_number = ?,

                student_name = ?,

                subjects = ?,

                marks = ?,

                total_marks = ?,

                overall_percentage = ?,

                best_5_total = ?,

                best_5_percentage = ?,

                result = ?

            WHERE academic_year = ?

            AND student_class = ?

            AND stream IS ?

            AND section = ?

            AND roll_number = ?
            """,

            (
                str(
                    student["Roll Number"]
                ),

                student["Student Name"],

                json.dumps(
                    subjects
                ),

                json.dumps(
                    marks
                ),

                int(
                    student["Total Marks"]
                ),

                float(
                    student["Overall Percentage"]
                ),

                int(
                    student["Best 5 Total"]
                ),

                float(
                    student["Best 5 Percentage"]
                ),

                student["Result"],

                academic_year,

                student_class,

                stream,

                section,

                str(
                    old_roll_number
                )
            )
        )

        updated_rows = cursor.rowcount

        connection.commit()

        return updated_rows > 0

    except Exception:

        connection.rollback()

        return False

    finally:

        connection.close()


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student(
    academic_year,
    student_class,
    stream,
    section,
    roll_number
):
    """
    Delete one student from SQLite.
    """

    connection = get_connection()

    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            DELETE FROM students

            WHERE academic_year = ?

            AND student_class = ?

            AND stream IS ?

            AND section = ?

            AND roll_number = ?
            """,

            (
                academic_year,

                student_class,

                stream,

                section,

                str(
                    roll_number
                )
            )
        )

        deleted_rows = cursor.rowcount

        connection.commit()

        return deleted_rows > 0

    except Exception:

        connection.rollback()

        return False

    finally:

        connection.close()


# ============================================================
# FIND ONE STUDENT
# ============================================================

def find_student(
    academic_year,
    student_class,
    stream,
    section,
    roll_number
):
    """
    Find one student using roll number.
    """

    connection = get_connection()

    cursor = connection.cursor()

    try:

        if stream is None:

            cursor.execute(
                """
                SELECT *

                FROM students

                WHERE academic_year = ?

                AND student_class = ?

                AND stream IS NULL

                AND section = ?

                AND roll_number = ?
                """,

                (
                    academic_year,
                    student_class,
                    section,
                    str(roll_number)
                )
            )

        else:

            cursor.execute(
                """
                SELECT *

                FROM students

                WHERE academic_year = ?

                AND student_class = ?

                AND stream = ?

                AND section = ?

                AND roll_number = ?
                """,

                (
                    academic_year,
                    student_class,
                    stream,
                    section,
                    str(roll_number)
                )
            )

        result = cursor.fetchone()

        return result

    finally:

        connection.close()


# ============================================================
# CLEAR ALL STUDENTS
# ============================================================

def clear_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM students
        """
    )

    connection.commit()

    connection.close()