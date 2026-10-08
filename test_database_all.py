# test_database_all.py

import sqlite3

from modules.database import (
    DATABASE_FILE,
    initialize_database
)


print("\n======================================")
print(" ALL SQLITE STUDENTS TEST")
print("======================================")


initialize_database()

connection = sqlite3.connect(
    DATABASE_FILE
)

cursor = connection.cursor()

cursor.execute(
    """
    SELECT
        id,
        academic_year,
        student_class,
        stream,
        section,
        roll_number,
        student_name,
        total_marks,
        best_5_percentage,
        result

    FROM students

    ORDER BY id
    """
)

rows = cursor.fetchall()

connection.close()


if not rows:

    print("\nSQLite database contains NO students.")

else:

    print(
        "\nStudents currently stored in SQLite:\n"
    )

    for row in rows:

        print(
            f"ID: {row[0]} | "
            f"Year: {row[1]} | "
            f"Class: {row[2]} | "
            f"Stream: {row[3]} | "
            f"Section: {row[4]} | "
            f"Roll: {row[5]} | "
            f"Name: {row[6]} | "
            f"Total: {row[7]} | "
            f"Best 5 %: {row[8]} | "
            f"Result: {row[9]}"
        )


print(
    f"\nTotal SQLite records: {len(rows)}"
)