# test_export.py

from modules.csv_manager import load_students
from modules.export import export_result_sheet


print("\n======================================")
print(" EXPORT TEST")
print("======================================")


dataframe = load_students(
    "2026-27",
    9,
    None,
    "A"
)


file_path = export_result_sheet(
    dataframe,
    "2026-27",
    9,
    None,
    "A"
)


if file_path:
    print("\nExport test completed successfully.")