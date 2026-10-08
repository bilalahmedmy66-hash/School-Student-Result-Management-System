from modules.csv_manager import load_students

from modules.search import (
    search_by_roll_number,
    search_by_name
)


def main():

    print("\n======================================")
    print(" VIEW AND SEARCH TEST")
    print("======================================")

    # Configuration
    academic_year = "2026-27"
    student_class = 9
    stream = None
    section = "A"

    # Load data
    dataframe = load_students(
        academic_year,
        student_class,
        stream,
        section
    )

    # ========================================================
    # VIEW ALL STUDENTS
    # ========================================================

    print("\n========== ALL STUDENTS ==========")

    if dataframe.empty:

        print("No students found.")

    else:

        print(
            dataframe.to_string(
                index=False
            )
        )

    # ========================================================
    # SEARCH BY ROLL NUMBER
    # ========================================================

    print("\n========== SEARCH BY ROLL NUMBER ==========")

    roll_number = input(
        "Enter Roll Number: "
    ).strip()

    result = search_by_roll_number(
        dataframe,
        roll_number
    )

    if result.empty:

        print("No student found.")

    else:

        print(
            result.to_string(
                index=False
            )
        )

    # ========================================================
    # SEARCH BY NAME
    # ========================================================

    print("\n========== SEARCH BY NAME ==========")

    name = input(
        "Enter Student Name: "
    ).strip()

    result = search_by_name(
        dataframe,
        name
    )

    if result.empty:

        print("No student found.")

    else:

        print(
            result.to_string(
                index=False
            )
        )


if __name__ == "__main__":
    main()