# main.py

"""
School Student Result Management System

Complete Console Application

Features:
1. Add Students
2. View All Students
3. Search Student
4. Show Topper
5. Show Statistics
6. Best 5 Percentage Graph
7. Subject Marks Graph
8. Export Result Sheet
9. Change Year/Class/Stream/Section
10. Edit Student
11. Delete Student
12. Exit

Storage:
- SQLite Database
- CSV Export

Analysis:
- Pandas
- Matplotlib
"""

# ============================================================
# CONFIGURATION
# ============================================================

from config import (
    get_academic_year,
    get_section
)


# ============================================================
# SUBJECTS
# ============================================================

from modules.subjects import (
    get_class,
    get_stream,
    get_subjects
)


# ============================================================
# STUDENT MANAGEMENT
# ============================================================

from modules.student_manager import (
    create_student_record,
    get_existing_roll_numbers
)


# ============================================================
# SEARCH
# ============================================================

from modules.search import (
    search_by_roll_number,
    search_by_name
)


# ============================================================
# TOPPER
# ============================================================

from modules.topper import (
    find_topper
)


# ============================================================
# STATISTICS
# ============================================================

from modules.statistics import (
    calculate_statistics
)


# ============================================================
# GRAPHS
# ============================================================

from modules.graphs import (
    show_best_5_percentage_graph,
    show_subject_marks_graph,
    get_subject_columns
)


# ============================================================
# EXPORT
# ============================================================

from modules.export import (
    export_result_sheet
)


# ============================================================
# DATABASE
# ============================================================

from modules.database import (
    initialize_database,
    insert_student_record,
    get_students_dataframe
)


# ============================================================
# CONFIGURATION SETUP
# ============================================================

def setup_configuration():

    print("\n")
    print("=" * 55)
    print(" SCHOOL RESULT SYSTEM - CONFIGURATION")
    print("=" * 55)

    academic_year = get_academic_year()

    student_class = get_class()

    stream = None

    if student_class in [11, 12]:

        stream = get_stream()

    section = get_section()

    print("\n========== SUBJECT CONFIGURATION ==========")

    subjects = get_subjects(
        student_class,
        stream
    )

    print("\nSelected Subjects:")

    for index, subject in enumerate(
        subjects,
        start=1
    ):
        print(
            f"{index}. {subject}"
        )

    return (
        academic_year,
        student_class,
        stream,
        section,
        subjects
    )


# ============================================================
# DISPLAY CONFIGURATION
# ============================================================

def display_configuration(
    academic_year,
    student_class,
    stream,
    section,
    subjects
):

    print("\n")
    print("=" * 65)
    print(" SCHOOL STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 65)

    print(
        f"Academic Year : {academic_year}"
    )

    print(
        f"Class         : {student_class}"
    )

    if stream:

        print(
            f"Stream        : {stream}"
        )

    print(
        f"Section       : {section}"
    )

    print(
        "\nSubjects:"
    )

    print(
        ", ".join(subjects)
    )

    print("=" * 65)


# ============================================================
# RELOAD DATA FROM SQLITE
# ============================================================

def reload_data(
    academic_year,
    student_class,
    stream,
    section
):

    return get_students_dataframe(
        academic_year,
        student_class,
        stream,
        section
    )


# ============================================================
# ADD STUDENTS
# ============================================================

def add_students(
    dataframe,
    academic_year,
    student_class,
    stream,
    section,
    subjects
):

    print("\n")
    print("=" * 55)
    print(" ADD STUDENTS")
    print("=" * 55)

    # --------------------------------------------------------
    # NUMBER OF STUDENTS
    # --------------------------------------------------------

    while True:

        number = input(
            "Enter number of students to add: "
        ).strip()

        if not number.isdigit():

            print(
                "Please enter a valid number."
            )

            continue

        number = int(number)

        if number <= 0:

            print(
                "Number of students must be greater than 0."
            )

            continue

        break

    # --------------------------------------------------------
    # EXISTING ROLL NUMBERS
    # --------------------------------------------------------

    existing_roll_numbers = (
        get_existing_roll_numbers(
            dataframe
        )
    )

    # --------------------------------------------------------
    # ADD STUDENTS
    # --------------------------------------------------------

    for i in range(number):

        print("\n")
        print("=" * 45)

        print(
            f"STUDENT {i + 1} OF {number}"
        )

        print("=" * 45)

        student = create_student_record(
            subjects,
            existing_roll_numbers
        )

        # ----------------------------------------------------
        # SAVE TO SQLITE
        # ----------------------------------------------------

        database_id = insert_student_record(
            academic_year,
            student_class,
            stream,
            section,
            student
        )

        if database_id is None:

            print(
                "\nERROR:"
                "\nStudent could not be saved."
            )

            print(
                "The roll number may already exist."
            )

            continue

        print(
            f"\nStudent saved to SQLite."
            f"\nDatabase ID: {database_id}"
        )

        existing_roll_numbers.add(
            str(
                student["Roll Number"]
            )
        )

        print(
            "\nStudent added successfully!"
        )

    # --------------------------------------------------------
    # RELOAD FROM DATABASE
    # --------------------------------------------------------

    dataframe = reload_data(
        academic_year,
        student_class,
        stream,
        section
    )

    return dataframe


# ============================================================
# VIEW ALL STUDENTS
# ============================================================

def view_all_students(dataframe):

    print("\n")
    print("=" * 55)
    print(" ALL STUDENTS")
    print("=" * 55)

    if dataframe is None or dataframe.empty:

        print(
            "No students found."
        )

        return

    print()

    print(
        dataframe.to_string(
            index=False
        )
    )


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student(dataframe):

    print("\n")
    print("=" * 55)
    print(" SEARCH STUDENT")
    print("=" * 55)

    if dataframe is None or dataframe.empty:

        print(
            "No student data available."
        )

        return

    print(
        "\n1. Search by Roll Number"
    )

    print(
        "2. Search by Student Name"
    )

    while True:

        choice = input(
            "Enter your choice (1-2): "
        ).strip()

        if choice in ["1", "2"]:

            break

        print(
            "Invalid choice."
        )

    # --------------------------------------------------------
    # ROLL SEARCH
    # --------------------------------------------------------

    if choice == "1":

        value = input(
            "Enter Roll Number: "
        ).strip()

        result = search_by_roll_number(
            dataframe,
            value
        )

    # --------------------------------------------------------
    # NAME SEARCH
    # --------------------------------------------------------

    else:

        value = input(
            "Enter Student Name: "
        ).strip()

        result = search_by_name(
            dataframe,
            value
        )

    print(
        "\n========== SEARCH RESULT =========="
    )

    if result.empty:

        print(
            "No matching student found."
        )

    else:

        print(
            result.to_string(
                index=False
            )
        )


# ============================================================
# SHOW TOPPER
# ============================================================

def show_topper(dataframe):

    print("\n")
    print("=" * 55)
    print(" TOPPER")
    print("=" * 55)

    topper = find_topper(
        dataframe
    )

    if topper.empty:

        print(
            "No student data available."
        )

        return

    print(
        "\n========== TOPPER =========="
    )

    print(
        topper.to_string(
            index=False
        )
    )


# ============================================================
# SHOW STATISTICS
# ============================================================

def show_statistics(dataframe):

    print("\n")
    print("=" * 55)
    print(" CLASS STATISTICS")
    print("=" * 55)

    statistics = calculate_statistics(
        dataframe
    )

    print()

    for key, value in statistics.items():

        print(
            f"{key}: {value}"
        )


# ============================================================
# BEST 5 GRAPH
# ============================================================

def best_5_graph(dataframe):

    print("\n")
    print("=" * 55)
    print(" BEST 5 PERCENTAGE GRAPH")
    print("=" * 55)

    if dataframe is None or dataframe.empty:

        print(
            "No student data available."
        )

        return

    file_path = (
        show_best_5_percentage_graph(
            dataframe
        )
    )

    if file_path:

        print(
            "\nGraph generated successfully."
        )

        print(
            f"Saved at: {file_path}"
        )


# ============================================================
# SUBJECT GRAPH
# ============================================================

def subject_graph(dataframe):

    print("\n")
    print("=" * 55)
    print(" SUBJECT MARKS GRAPH")
    print("=" * 55)

    if dataframe is None or dataframe.empty:

        print(
            "No student data available."
        )

        return

    subjects = get_subject_columns(
        dataframe
    )

    if not subjects:

        print(
            "No subjects available."
        )

        return

    print(
        "\n========== SUBJECTS =========="
    )

    for index, subject in enumerate(
        subjects,
        start=1
    ):

        print(
            f"{index}. {subject}"
        )

    while True:

        choice = input(
            f"Select subject (1-{len(subjects)}): "
        ).strip()

        if not choice.isdigit():

            print(
                "Please enter a valid number."
            )

            continue

        choice = int(choice)

        if 1 <= choice <= len(subjects):

            selected_subject = subjects[
                choice - 1
            ]

            break

        print(
            "Invalid subject selection."
        )

    file_path = (
        show_subject_marks_graph(
            dataframe,
            selected_subject
        )
    )

    if file_path:

        print(
            "\nSubject graph generated successfully."
        )

        print(
            f"Saved at: {file_path}"
        )


# ============================================================
# EXPORT RESULT
# ============================================================

def export_result(
    dataframe,
    academic_year,
    student_class,
    stream,
    section
):

    print("\n")
    print("=" * 55)
    print(" EXPORT RESULT SHEET")
    print("=" * 55)

    if dataframe is None or dataframe.empty:

        print(
            "No student data available."
        )

        return

    file_path = export_result_sheet(
        dataframe,
        academic_year,
        student_class,
        stream,
        section
    )

    if file_path:

        print(
            "\nExport completed successfully."
        )

        print(
            f"File: {file_path}"
        )


# ============================================================
# EDIT STUDENT
# ============================================================

def edit_student(
    dataframe,
    academic_year,
    student_class,
    stream,
    section,
    subjects
):

    print("\n")
    print("=" * 55)
    print(" EDIT STUDENT")
    print("=" * 55)

    if dataframe is None or dataframe.empty:

        print(
            "No students available."
        )

        return dataframe

    roll_number = input(
        "Enter Roll Number of student to edit: "
    ).strip()

    result = search_by_roll_number(
        dataframe,
        roll_number
    )

    if result.empty:

        print(
            "Student not found."
        )

        return dataframe

    print(
        "\nCurrent Student:"
    )

    print(
        result.to_string(
            index=False
        )
    )

    print(
        "\nFor editing, the student record "
        "will be recreated."
    )

    confirm = input(
        "Continue? (Y/N): "
    ).strip().upper()

    if confirm != "Y":

        print(
            "Edit cancelled."
        )

        return dataframe

    # --------------------------------------------------------
    # DELETE OLD RECORD
    # --------------------------------------------------------

    from modules.database import delete_student

    deleted = delete_student(
        academic_year,
        student_class,
        stream,
        section,
        roll_number
    )

    if not deleted:

        print(
            "Could not delete the old record."
        )

        return dataframe

    # --------------------------------------------------------
    # CREATE UPDATED RECORD
    # --------------------------------------------------------

    existing_roll_numbers = (
        get_existing_roll_numbers(
            dataframe
        )
    )

    existing_roll_numbers.discard(
        str(roll_number)
    )

    print(
        "\nEnter updated student details."
    )

    student = create_student_record(
        subjects,
        existing_roll_numbers
    )

    database_id = insert_student_record(
        academic_year,
        student_class,
        stream,
        section,
        student
    )

    if database_id is None:

        print(
            "\nERROR: Updated student could not be saved."
        )

    else:

        print(
            "\nStudent updated successfully!"
        )

    return reload_data(
        academic_year,
        student_class,
        stream,
        section
    )


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student_record(
    dataframe,
    academic_year,
    student_class,
    stream,
    section
):

    print("\n")
    print("=" * 55)
    print(" DELETE STUDENT")
    print("=" * 55)

    if dataframe is None or dataframe.empty:

        print(
            "No students available."
        )

        return dataframe

    roll_number = input(
        "Enter Roll Number to delete: "
    ).strip()

    result = search_by_roll_number(
        dataframe,
        roll_number
    )

    if result.empty:

        print(
            "Student not found."
        )

        return dataframe

    print(
        "\nStudent to be deleted:"
    )

    print(
        result.to_string(
            index=False
        )
    )

    confirm = input(
        "\nAre you sure you want to delete "
        "this student? (Y/N): "
    ).strip().upper()

    if confirm != "Y":

        print(
            "Delete cancelled."
        )

        return dataframe

    from modules.database import delete_student

    deleted = delete_student(
        academic_year,
        student_class,
        stream,
        section,
        roll_number
    )

    if deleted:

        print(
            "\nStudent deleted successfully."
        )

    else:

        print(
            "\nStudent could not be deleted."
        )

    return reload_data(
        academic_year,
        student_class,
        stream,
        section
    )


# ============================================================
# MAIN
# ============================================================

def main():

    # --------------------------------------------------------
    # INITIALIZE DATABASE
    # --------------------------------------------------------

    initialize_database()

    # --------------------------------------------------------
    # SETUP
    # --------------------------------------------------------

    (
        academic_year,
        student_class,
        stream,
        section,
        subjects
    ) = setup_configuration()

    # --------------------------------------------------------
    # LOAD FROM SQLITE
    # --------------------------------------------------------

    dataframe = reload_data(
        academic_year,
        student_class,
        stream,
        section
    )

    # ========================================================
    # MAIN MENU
    # ========================================================

    while True:

        display_configuration(
            academic_year,
            student_class,
            stream,
            section,
            subjects
        )

        print(
            "\n=============== MAIN MENU ==============="
        )

        print(
            "1. Add Students"
        )

        print(
            "2. View All Students"
        )

        print(
            "3. Search Student"
        )

        print(
            "4. Show Topper"
        )

        print(
            "5. Show Statistics"
        )

        print(
            "6. Best 5 Percentage Graph"
        )

        print(
            "7. Subject Marks Graph"
        )

        print(
            "8. Export Result Sheet"
        )

        print(
            "9. Change Year/Class/Stream/Section"
        )

        print(
            "10. Edit Student"
        )

        print(
            "11. Delete Student"
        )

        print(
            "12. Exit"
        )

        choice = input(
            "\nEnter your choice (1-12): "
        ).strip()

        # ====================================================
        # 1. ADD STUDENTS
        # ====================================================

        if choice == "1":

            dataframe = add_students(
                dataframe,
                academic_year,
                student_class,
                stream,
                section,
                subjects
            )

        # ====================================================
        # 2. VIEW ALL
        # ====================================================

        elif choice == "2":

            view_all_students(
                dataframe
            )

        # ====================================================
        # 3. SEARCH
        # ====================================================

        elif choice == "3":

            search_student(
                dataframe
            )

        # ====================================================
        # 4. TOPPER
        # ====================================================

        elif choice == "4":

            show_topper(
                dataframe
            )

        # ====================================================
        # 5. STATISTICS
        # ====================================================

        elif choice == "5":

            show_statistics(
                dataframe
            )

        # ====================================================
        # 6. BEST 5 GRAPH
        # ====================================================

        elif choice == "6":

            best_5_graph(
                dataframe
            )

        # ====================================================
        # 7. SUBJECT GRAPH
        # ====================================================

        elif choice == "7":

            subject_graph(
                dataframe
            )

        # ====================================================
        # 8. EXPORT
        # ====================================================

        elif choice == "8":

            export_result(
                dataframe,
                academic_year,
                student_class,
                stream,
                section
            )

        # ====================================================
        # 9. CHANGE CONFIGURATION
        # ====================================================

        elif choice == "9":

            print(
                "\nChanging configuration..."
            )

            (
                academic_year,
                student_class,
                stream,
                section,
                subjects
            ) = setup_configuration()

            dataframe = reload_data(
                academic_year,
                student_class,
                stream,
                section
            )

        # ====================================================
        # 10. EDIT
        # ====================================================

        elif choice == "10":

            dataframe = edit_student(
                dataframe,
                academic_year,
                student_class,
                stream,
                section,
                subjects
            )

        # ====================================================
        # 11. DELETE
        # ====================================================

        elif choice == "11":

            dataframe = delete_student_record(
                dataframe,
                academic_year,
                student_class,
                stream,
                section
            )

        # ====================================================
        # 12. EXIT
        # ====================================================

        elif choice == "12":

            print("\n")
            print("=" * 55)

            print(
                "Thank you for using the "
                "School Student Result Management System!"
            )

            print("=" * 55)

            break

        # ====================================================
        # INVALID OPTION
        # ====================================================

        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please select an option from 1 to 12."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()