from config import (
    get_academic_year,
    get_section,
    generate_csv_filename
)


def main():

    print("\n======================================")
    print(" CONFIGURATION TEST")
    print("======================================")

    # Academic year
    academic_year = get_academic_year()

    # Class
    while True:

        print("\n========== CLASS SELECTION ==========")
        print("1. Class 9")
        print("2. Class 10")
        print("3. Class 11")
        print("4. Class 12")

        choice = input("Enter your choice (1-4): ").strip()

        if choice in ["1", "2", "3", "4"]:
            student_class = int(choice) + 8
            break

        print("Invalid choice. Please select 1-4.")

    # Stream
    stream = None

    if student_class in [11, 12]:

        print("\n========== STREAM ==========")
        print("1. Science")
        print("2. Commerce")
        print("3. Arts/Humanities")

        while True:

            choice = input("Enter stream (1-3): ").strip()

            if choice == "1":
                stream = "Science"
                break

            elif choice == "2":
                stream = "Commerce"
                break

            elif choice == "3":
                stream = "Arts/Humanities"
                break

            print("Invalid stream choice.")

    # Section
    section = get_section()

    # Generate filename
    filename = generate_csv_filename(
        academic_year,
        student_class,
        stream,
        section
    )

    print("\n======================================")
    print(" CONFIGURATION RESULT")
    print("======================================")

    print("Academic Year :", academic_year)
    print("Class         :", student_class)
    print("Stream        :", stream)
    print("Section       :", section)
    print("CSV Filename  :", filename)


if __name__ == "__main__":
    main()