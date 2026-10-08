from modules.student_manager import (
    create_student_record
)


def main():

    print("\n======================================")
    print(" STUDENT RECORD TEST")
    print("======================================")

    subjects = [
        "English",
        "Hindi",
        "Mathematics",
        "Science",
        "Social Science",
        "Information Technology"
    ]

    existing_roll_numbers = set()

    student = create_student_record(
        subjects,
        existing_roll_numbers
    )

    print("\n========== STUDENT RESULT ==========")

    for key, value in student.items():

        if "Percentage" in key:

            print(f"{key}: {value}%")

        else:

            print(f"{key}: {value}")


if __name__ == "__main__":
    main()