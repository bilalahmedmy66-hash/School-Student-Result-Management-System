from modules.csv_manager import (
    load_students,
    add_student_to_csv
)


def main():

    print("\n======================================")
    print(" CSV STORAGE TEST")
    print("======================================")

    # Project configuration
    academic_year = "2026-27"
    student_class = 9
    stream = None
    section = "A"

    # Test student
    student = {
        "Roll Number": "101",
        "Student Name": "Bilal Ahmed",
        "English": 40,
        "Hindi": 60,
        "Mathematics": 20,
        "Science": 40,
        "Social Science": 60,
        "Information Technology": 50,
        "Total Marks": 270,
        "Overall Percentage": 45.0,
        "Best 5 Total": 250,
        "Best 5 Percentage": 50.0,
        "Result": "FAIL"
    }

    # Save student
    dataframe, csv_path = add_student_to_csv(
        student,
        academic_year,
        student_class,
        stream,
        section
    )

    print("\nStudent saved successfully!")

    print("\nCSV File:")
    print(csv_path)

    print("\n========== SAVED DATA ==========")

    print(dataframe.to_string(index=False))

    # Load again from CSV
    print("\n========== LOADING FROM CSV ==========")

    loaded_dataframe = load_students(
        academic_year,
        student_class,
        stream,
        section
    )

    print(
        loaded_dataframe.to_string(
            index=False
        )
    )


if __name__ == "__main__":
    main()