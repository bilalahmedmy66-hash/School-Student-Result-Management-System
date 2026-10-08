from modules.csv_manager import load_students
from modules.topper import find_topper


def main():

    print("\n======================================")
    print(" TOPPER TEST")
    print("======================================")

    academic_year = "2026-27"
    student_class = 9
    stream = None
    section = "A"

    dataframe = load_students(
        academic_year,
        student_class,
        stream,
        section
    )

    topper = find_topper(dataframe)

    if topper.empty:

        print("No students available.")

    else:

        print("\n========== TOPPER ==========")

        print(
            topper.to_string(
                index=False
            )
        )


if __name__ == "__main__":
    main()