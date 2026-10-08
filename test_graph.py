# test_graph.py

from modules.csv_manager import load_students
from modules.graphs import (
    show_best_5_percentage_graph,
    show_subject_marks_graph,
    get_subject_columns
)


print("\n======================================")
print(" GRAPH TEST")
print("======================================")


dataframe = load_students(
    "2026-27",
    9,
    None,
    "A"
)


print("\n========== SUBJECTS ==========")

subjects = get_subject_columns(
    dataframe
)

for subject in subjects:
    print(subject)


print("\n========== BEST 5 GRAPH ==========")

show_best_5_percentage_graph(
    dataframe
)


print("\n========== SUBJECT GRAPH ==========")

show_subject_marks_graph(
    dataframe,
    "English"
)