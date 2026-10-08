from modules.validation import (
    validate_name,
    validate_roll_number,
    validate_marks
)


def main():

    print("\n======================================")
    print(" VALIDATION TEST")
    print("======================================")

    # Name tests
    print("\n--- NAME TESTS ---")

    test_names = [
        "Bilal Ahmed",
        "",
        "Bilal123",
        "Ahmed@123"
    ]

    for name in test_names:

        valid, result = validate_name(name)

        print(
            f"Input: '{name}'"
            f" → Valid: {valid}"
            f" → {result}"
        )

    # Roll number tests
    print("\n--- ROLL NUMBER TESTS ---")

    test_roll_numbers = [
        "101",
        "",
        "A101",
        "10 1",
        "10@1"
    ]

    for roll_number in test_roll_numbers:

        valid, result = validate_roll_number(
            roll_number
        )

        print(
            f"Input: '{roll_number}'"
            f" → Valid: {valid}"
            f" → {result}"
        )

    # Marks tests
    print("\n--- MARKS TESTS ---")

    test_marks = [
        "95",
        "0",
        "100",
        "33",
        "101",
        "-5",
        "",
        "abc"
    ]

    for mark in test_marks:

        valid, result = validate_marks(mark)

        print(
            f"Input: '{mark}'"
            f" → Valid: {valid}"
            f" → {result}"
        )


if __name__ == "__main__":
    main()