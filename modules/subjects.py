# modules/subjects.py

"""
Subject Selection Module
School Student Result Management System

Handles:
- Class selection
- Stream selection
- Language selection
- Science Maths/Biology selection
- Class 9/10 optional subject selection
- Automatic subject generation
"""


# ============================================================
# CLASS SELECTION
# ============================================================

def get_class():
    """Ask the user to select Class 9, 10, 11 or 12."""

    while True:
        print("\n========== CLASS SELECTION ==========")
        print("1. Class 9")
        print("2. Class 10")
        print("3. Class 11")
        print("4. Class 12")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            return 9

        elif choice == "2":
            return 10

        elif choice == "3":
            return 11

        elif choice == "4":
            return 12

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


# ============================================================
# STREAM SELECTION
# ============================================================

def get_stream():
    """Ask the user to select a stream for Class 11 or 12."""

    while True:
        print("\n========== STREAM SELECTION ==========")
        print("1. Science")
        print("2. Commerce")
        print("3. Arts/Humanities")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            return "Science"

        elif choice == "2":
            return "Commerce"

        elif choice == "3":
            return "Arts/Humanities"

        else:
            print("Invalid choice. Please select 1, 2 or 3.")


# ============================================================
# LANGUAGE SELECTION
# ============================================================

def get_language():
    """
    For Classes 11 and 12, exactly ONE language
    must be selected.
    """

    while True:
        print("\n========== LANGUAGE SELECTION ==========")
        print("1. English")
        print("2. Hindi")

        choice = input("Select ONE language (1-2): ").strip()

        if choice == "1":
            return "English"

        elif choice == "2":
            return "Hindi"

        else:
            print("Invalid choice. Please select 1 or 2.")


# ============================================================
# SCIENCE SUBJECT SELECTION
# ============================================================

def get_science_optional_subject():
    """
    Science students must select exactly ONE:
    Maths OR Biology.
    """

    while True:
        print("\n========== SCIENCE SUBJECT ==========")
        print("1. Maths")
        print("2. Biology")

        choice = input("Select ONE subject (1-2): ").strip()

        if choice == "1":
            return "Maths"

        elif choice == "2":
            return "Biology"

        else:
            print("Invalid choice. Please select 1 or 2.")


# ============================================================
# CLASS 9/10 OPTIONAL SUBJECT
# ============================================================

def get_class_9_10_optional_subject():
    """
    Class 9 and 10 students have the five core subjects
    plus ONE optional subject.

    Selecting 'None' is allowed if the school/student
    does not use an additional optional subject.
    """

    optional_subjects = [
        "None",
        "Information Technology",
        "Artificial Intelligence",
        "Sanskrit",
        "French",
        "Physical Education",
        "Painting"
    ]

    while True:

        print("\n========== OPTIONAL SUBJECT ==========")

        for index, subject in enumerate(
            optional_subjects,
            start=1
        ):
            print(f"{index}. {subject}")

        choice = input(
            f"Select ONE optional subject (1-{len(optional_subjects)}): "
        ).strip()

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(optional_subjects):
            selected_subject = optional_subjects[choice - 1]

            if selected_subject == "None":
                return None

            return selected_subject

        print(
            f"Invalid choice. Please select 1-{len(optional_subjects)}."
        )


# ============================================================
# SUBJECT GENERATOR
# ============================================================

def get_subjects(student_class, stream=None):
    """
    Automatically generate the complete subject list
    according to class and stream.
    """

    # ========================================================
    # CLASS 9 AND 10
    # ========================================================

    if student_class in [9, 10]:

        core_subjects = [
            "English",
            "Hindi",
            "Mathematics",
            "Science",
            "Social Science"
        ]

        optional_subject = get_class_9_10_optional_subject()

        if optional_subject is not None:
            core_subjects.append(optional_subject)

        return core_subjects

    # ========================================================
    # CLASS 11 AND 12
    # ========================================================

    if student_class in [11, 12]:

        if stream is None:
            raise ValueError(
                "Stream is required for Class 11 and 12."
            )

        # ----------------------------------------------------
        # SCIENCE
        # ----------------------------------------------------

        if stream == "Science":

            language = get_language()

            optional_subject = get_science_optional_subject()

            return [
                language,
                "Physics",
                "Chemistry",
                optional_subject,
                "Computer Science",
                "Physical Education"
            ]

        # ----------------------------------------------------
        # COMMERCE
        # ----------------------------------------------------

        elif stream == "Commerce":

            language = get_language()

            return [
                language,
                "Accounts",
                "Business Studies",
                "Economics",
                "Maths",
                "Informatics Practices",
                "Physical Education"
            ]

        # ----------------------------------------------------
        # ARTS / HUMANITIES
        # ----------------------------------------------------

        elif stream == "Arts/Humanities":

            language = get_language()

            return [
                language,
                "History",
                "Political Science",
                "Geography",
                "Economics",
                "Sociology"
            ]

        else:
            raise ValueError("Invalid stream.")

    raise ValueError("Invalid class.")