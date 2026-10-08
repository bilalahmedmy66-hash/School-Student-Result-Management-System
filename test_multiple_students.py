from modules.student_manager import (
    create_student_record,
    get_existing_roll_numbers
)

from modules.csv_manager import (
    load_students,
    add_student_to_csv
)


def main():

    print("\n======================================")
    print(" MULTIPLE STUDENT TEST")
    print("======================================")

    # Configuration
    academic_year = "2026-27"
    student_class = 9
    stream = None
    section = "A"

    subjects = [
        "English",
        "Hindi",
        "Mathematics",
        "Science",
        "Social Science",
        "Information Technology"
    ]

    # Load existing students
    dataframe = load_students(
        academic_year,
        student_class,
        stream,
        section
    )

    # Get existing roll numbers
    existing_roll_numbers = (
        get_existing_roll_numbers(
            dataframe
        )
    )

    print(
        "\nExisting Roll Numbers:",
        existing_roll_numbers
    )

    # Number of students
    while True:

        number = input(
            "\nHow many students do you want to add? "
        ).strip()

        if number.isdigit():

            number = int(number)

            if number > 0:
                break

        print(
            "Please enter a positive whole number."
        )

    # Add students
    for student_number in range(
        1,
        number + 1
    ):

        print(
            f"\n\n========== STUDENT "
            f"{student_number} OF {number} =========="
        )

        student = create_student_record(
            subjects,
            existing_roll_numbers
        )

        # Save student
        dataframe, csv_path = (
            add_student_to_csv(
                student,
                academic_year,
                student_class,
                stream,
                section
            )
        )

        # Update roll numbers
        existing_roll_numbers = (
            get_existing_roll_numbers(
                dataframe
            )
        )

        print(
            "\nStudent saved successfully!"
        )

        print(
            "CSV File:",
            csv_path
        )

    # Final display
    print(
        "\n======================================"
    )

    print(
        " FINAL STUDENT DATA"
    )

    print(
        "======================================"
    )

    print(
        dataframe.to_string(
            index=False
        )
    )


if __name__ == "__main__":
    main()