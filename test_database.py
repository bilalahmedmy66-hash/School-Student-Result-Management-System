# test_database.py

import sqlite3

from modules.database import (
    initialize_database,
    DATABASE_FILE,
    count_students
)


print("\n======================================")
print(" DATABASE TEST")
print("======================================")


# Create database and table
initialize_database()


print(
    f"\nDatabase location:"
    f"\n{DATABASE_FILE}"
)


# Check student count
print(
    f"\nTotal students currently in database: "
    f"{count_students()}"
)


# Verify tables
connection = sqlite3.connect(
    DATABASE_FILE
)

cursor = connection.cursor()

cursor.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    """
)

tables = cursor.fetchall()

connection.close()


print("\n========== DATABASE TABLES ==========")

for table in tables:
    print(
        f"Table: {table[0]}"
    )


if any(table[0] == "students" for table in tables):

    print(
        "\nSUCCESS: students table exists."
    )

else:

    print(
        "\nERROR: students table was not found."
    )


print(
    "\nDatabase test completed successfully."
)