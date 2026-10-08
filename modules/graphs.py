# modules/graphs.py

"""
Graph Module
School Student Result Management System

Generates:
1. Best 5 Percentage Graph
2. Subject Marks Graph
"""

import os
import matplotlib.pyplot as plt
import pandas as pd


GRAPH_FOLDER = "exports"


def create_graph_folder():

    if not os.path.exists(GRAPH_FOLDER):
        os.makedirs(GRAPH_FOLDER)


def show_best_5_percentage_graph(dataframe):

    if dataframe is None or dataframe.empty:
        print("No student data available.")
        return None

    create_graph_folder()

    names = dataframe["Student Name"].astype(str)

    percentages = pd.to_numeric(
        dataframe["Best 5 Percentage"],
        errors="coerce"
    )

    plt.figure(figsize=(10, 6))

    plt.bar(
        names,
        percentages
    )

    plt.title(
        "Best 5 Percentage - Student Performance"
    )

    plt.xlabel(
        "Student Name"
    )

    plt.ylabel(
        "Best 5 Percentage"
    )

    plt.ylim(0, 100)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    file_path = os.path.join(
        GRAPH_FOLDER,
        "best_5_percentage.png"
    )

    plt.savefig(file_path)

    plt.close()

    print(
        f"Best 5 graph saved: {file_path}"
    )

    return file_path


def show_subject_marks_graph(
    dataframe,
    subject
):

    if dataframe is None or dataframe.empty:
        print("No student data available.")
        return None

    if subject not in dataframe.columns:
        print(
            f"Subject '{subject}' does not exist."
        )
        return None

    create_graph_folder()

    names = dataframe["Student Name"].astype(str)

    marks = pd.to_numeric(
        dataframe[subject],
        errors="coerce"
    )

    plt.figure(figsize=(10, 6))

    plt.bar(
        names,
        marks
    )

    plt.title(
        f"{subject} - Student Marks"
    )

    plt.xlabel(
        "Student Name"
    )

    plt.ylabel(
        "Marks"
    )

    plt.ylim(0, 100)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    safe_subject = subject.replace(
        " ",
        "_"
    )

    file_path = os.path.join(
        GRAPH_FOLDER,
        f"{safe_subject}_marks.png"
    )

    plt.savefig(file_path)

    plt.close()

    print(
        f"Subject graph saved: {file_path}"
    )

    return file_path


def get_subject_columns(dataframe):

    excluded_columns = {
        "Roll Number",
        "Student Name",
        "Total Marks",
        "Overall Percentage",
        "Best 5 Total",
        "Best 5 Percentage",
        "Result"
    }

    return [
        column
        for column in dataframe.columns
        if column not in excluded_columns
    ]