from modules.calculations import (
    calculate_total,
    calculate_percentage,
    calculate_best_5_total,
    calculate_best_5_percentage,
    calculate_result,
    calculate_complete_result
)


def main():

    print("\n======================================")
    print(" RESULT CALCULATION TEST")
    print("======================================")

    marks = {
        "English": 85,
        "Hindi": 78,
        "Mathematics": 92,
        "Science": 88,
        "Social Science": 81,
        "Information Technology": 95
    }

    print("\nSubject Marks:")

    for subject, mark in marks.items():
        print(f"{subject}: {mark}")

    # Individual calculations
    total = calculate_total(marks)

    percentage = calculate_percentage(marks)

    best_5_total = calculate_best_5_total(marks)

    best_5_percentage = calculate_best_5_percentage(marks)

    result = calculate_result(marks)

    print("\n========== CALCULATION RESULT ==========")

    print("Total Marks:", total)

    print("Overall Percentage:", percentage)

    print("Best 5 Total:", best_5_total)

    print("Best 5 Percentage:", best_5_percentage)

    print("Result:", result)

    # Complete calculation
    print("\n========== COMPLETE RESULT ==========")

    complete_result = calculate_complete_result(marks)

    for key, value in complete_result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()