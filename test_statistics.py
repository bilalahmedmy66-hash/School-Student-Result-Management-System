# test_statistics.py

from modules.csv_manager import load_students
from modules.statistics import calculate_statistics


print("\n======================================")
print(" STATISTICS TEST")
print("======================================")

dataframe = load_students(
    "2026-27",
    9,
    None,
    "A"
)

statistics = calculate_statistics(
    dataframe
)

print("\n========== STATISTICS ==========")

for key, value in statistics.items():
    print(f"{key}: {value}")