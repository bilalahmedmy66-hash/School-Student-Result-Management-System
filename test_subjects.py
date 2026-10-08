from modules.subjects import get_class, get_stream, get_subjects


def main():

    print("\n======================================")
    print(" SCHOOL RESULT MANAGEMENT SYSTEM")
    print(" SUBJECT SELECTION TEST")
    print("======================================")

    student_class = get_class()

    stream = None

    if student_class in [11, 12]:
        stream = get_stream()

    subjects = get_subjects(student_class, stream)

    print("\n========== FINAL SUBJECTS ==========")

    for number, subject in enumerate(subjects, start=1):
        print(f"{number}. {subject}")

    print("\nTotal Subjects:", len(subjects))


if __name__ == "__main__":
    main()