# test_database_read.py

from modules.database import (
    initialize_database,
    get_students_dataframe
)


print("\n======================================")
print(" SQLITE READ TEST")
print("======================================")


initialize_database()


dataframe = get_students_dataframe(
    "2026-27",
    9,
    None,
    "A"
)


if dataframe.empty:

    print("\nNo students found in SQLite.")

else:

    print("\nStudents retrieved from SQLite:")

    print(
        dataframe.to_string(
            index=False
        )
    )


print("\nSQLite read test completed.")