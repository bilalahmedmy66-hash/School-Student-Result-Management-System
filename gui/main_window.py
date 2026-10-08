import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# PROJECT MODULES
# ============================================================

from modules.database import (
    initialize_database,
    get_students_dataframe,
    insert_student_record,
    update_student,
    delete_student
)

from modules.calculations import (
    calculate_complete_result
)


# ============================================================
# COLORS
# ============================================================

BG = "#F4F7FB"
WHITE = "#FFFFFF"
DARK = "#172033"
SIDEBAR = "#172033"
ACTIVE = "#263552"
BLUE = "#2563EB"
BLUE_DARK = "#1D4ED8"
GREEN = "#16A34A"
RED = "#DC2626"
PURPLE = "#7C3AED"
GRAY = "#6B7280"
LIGHT_BORDER = "#E5E7EB"


# ============================================================
# SUBJECT CONFIGURATION
# ============================================================

CLASS_9_10_CORE = [
    "English",
    "Hindi",
    "Mathematics",
    "Science",
    "Social Science"
]

OPTIONAL_SUBJECTS = [
    "None",
    "Information Technology",
    "Artificial Intelligence",
    "Sanskrit",
    "French",
    "Physical Education",
    "Painting"
]

STREAMS = [
    "Science",
    "Commerce",
    "Arts/Humanities"
]

LANGUAGES = [
    "English",
    "Hindi"
]

SCIENCE_CHOICES = [
    "Mathematics",
    "Biology"
]


def build_subjects(
    student_class,
    stream=None,
    language="English",
    science_choice="Mathematics",
    optional_subject="None"
):

    if student_class in (9, 10):

        subjects = list(
            CLASS_9_10_CORE
        )

        if optional_subject != "None":

            subjects.append(
                optional_subject
            )

        return subjects

    if student_class == 11:

        selected_language = language

        subjects = [
            selected_language,
            "Physics",
            "Chemistry",
            science_choice,
            "Computer Science",
            "Physical Education"
        ]

        return subjects

    if student_class == 12:

        selected_language = language

        subjects = [
            selected_language,
            "Physics",
            "Chemistry",
            science_choice,
            "Computer Science",
            "Physical Education"
        ]

        return subjects

    if stream == "Commerce":

        return [
            language,
            "Accounts",
            "Business Studies",
            "Economics",
            "Mathematics",
            "Informatics Practices",
            "Physical Education"
        ]

    if stream == "Arts/Humanities":

        return [
            language,
            "History",
            "Political Science",
            "Geography",
            "Economics",
            "Sociology"
        ]

    return [
        language,
        "Physics",
        "Chemistry",
        science_choice,
        "Computer Science",
        "Physical Education"
    ]


def build_subjects_for_configuration(
    student_class,
    stream,
    language,
    science_choice,
    optional_subject
):

    if student_class in (9, 10):

        subjects = list(
            CLASS_9_10_CORE
        )

        if optional_subject != "None":

            subjects.append(
                optional_subject
            )

        return subjects

    if stream == "Science":

        return [
            language,
            "Physics",
            "Chemistry",
            science_choice,
            "Computer Science",
            "Physical Education"
        ]

    if stream == "Commerce":

        return [
            language,
            "Accounts",
            "Business Studies",
            "Economics",
            "Mathematics",
            "Informatics Practices",
            "Physical Education"
        ]

    return [
        language,
        "History",
        "Political Science",
        "Geography",
        "Economics",
        "Sociology"
    ]


# ============================================================
# MAIN GUI
# ============================================================

class SchoolResultGUI:

    def __init__(
        self,
        root,
        academic_year,
        student_class,
        stream,
        section,
        language="English",
        science_choice="Mathematics",
        optional_subject="None"
    ):

        self.root = root

        self.academic_year = academic_year
        self.student_class = student_class
        self.stream = stream
        self.section = section
        self.language = language
        self.science_choice = science_choice
        self.optional_subject = optional_subject

        self.subjects = build_subjects_for_configuration(
            student_class,
            stream,
            language,
            science_choice,
            optional_subject
        )

        self.selected_roll = None

        initialize_database()

        self.root.title(
            "School Student Result Management System"
        )

        self.root.geometry(
            "1350x780"
        )

        self.root.minsize(
            1100,
            650
        )

        self.root.configure(
            bg=BG
        )

        self.setup_styles()
        self.build_interface()
        self.show_dashboard()

    # ========================================================
    # STYLES
    # ========================================================

    def setup_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Treeview",
            background=WHITE,
            foreground=DARK,
            fieldbackground=WHITE,
            rowheight=34,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#E8EEF8",
            foreground=DARK,
            font=("Segoe UI Semibold", 10)
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#DBEAFE")
            ]
        )

    # ========================================================
    # MAIN INTERFACE
    # ========================================================

    def build_interface(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=SIDEBAR,
            width=235
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        logo = tk.Frame(
            self.sidebar,
            bg=SIDEBAR
        )

        logo.pack(
            fill="x",
            padx=20,
            pady=25
        )

        tk.Label(
            logo,
            text="SR",
            font=("Segoe UI Bold", 23),
            fg="white",
            bg=BLUE,
            width=3,
            pady=5
        ).pack(
            side="left"
        )

        title = tk.Frame(
            logo,
            bg=SIDEBAR
        )

        title.pack(
            side="left",
            padx=10
        )

        tk.Label(
            title,
            text="School Result",
            font=("Segoe UI Semibold", 12),
            fg="white",
            bg=SIDEBAR
        ).pack(
            anchor="w"
        )

        tk.Label(
            title,
            text="Management System",
            font=("Segoe UI", 8),
            fg="#AEB8CA",
            bg=SIDEBAR
        ).pack(
            anchor="w"
        )

        self.nav_buttons = {}

        navigation = [
            ("Dashboard", self.show_dashboard),
            ("Students", self.show_students),
            ("Add Student", self.add_student),
            ("Search Student", self.search_student),
            ("Topper", self.show_topper),
            ("Statistics", self.show_statistics),
            ("Graphs", self.show_graphs),
            ("Export Result", self.export_result),
            ("Settings", self.show_settings)
        ]

        for name, command in navigation:

            self.create_nav_button(
                name,
                command
            )

        self.main = tk.Frame(
            self.root,
            bg=BG
        )

        self.main.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.header = tk.Frame(
            self.main,
            bg=WHITE,
            height=75
        )

        self.header.pack(
            fill="x"
        )

        self.header.pack_propagate(False)

        self.header_title = tk.Label(
            self.header,
            text="Dashboard",
            font=("Segoe UI Semibold", 20),
            fg=DARK,
            bg=WHITE
        )

        self.header_title.pack(
            side="left",
            padx=30
        )

        self.config_label = tk.Label(
            self.header,
            text="",
            font=("Segoe UI", 10),
            fg=GRAY,
            bg=WHITE
        )

        self.config_label.pack(
            side="right",
            padx=30
        )

        self.update_config_label()

        self.content = tk.Frame(
            self.main,
            bg=BG
        )

        self.content.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

    # ========================================================
    # NAVIGATION BUTTON
    # ========================================================

    def create_nav_button(
        self,
        text,
        command
    ):

        button = tk.Button(
            self.sidebar,
            text=text,
            command=command,
            font=("Segoe UI", 10),
            fg="white",
            bg=SIDEBAR,
            activebackground=ACTIVE,
            activeforeground="white",
            relief="flat",
            bd=0,
            anchor="w",
            padx=25,
            pady=12,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=10,
            pady=2
        )

        self.nav_buttons[text] = button

    def activate_nav(self, name):

        for button_name, button in self.nav_buttons.items():

            button.config(
                bg=(
                    ACTIVE
                    if button_name == name
                    else SIDEBAR
                )
            )

    # ========================================================
    # CONFIGURATION LABEL
    # ========================================================

    def update_config_label(self):

        if self.stream:

            text = (
                f"{self.academic_year} • "
                f"Class {self.student_class} • "
                f"{self.stream} • "
                f"Section {self.section}"
            )

        else:

            text = (
                f"{self.academic_year} • "
                f"Class {self.student_class} • "
                f"Section {self.section}"
            )

        self.config_label.config(
            text=text
        )

    # ========================================================
    # CONTENT CLEAR
    # ========================================================

    def clear_content(self):

        for widget in self.content.winfo_children():

            widget.destroy()

    # ========================================================
    # DATABASE DATA
    # ========================================================

    def get_data(self):

        try:

            return get_students_dataframe(
                self.academic_year,
                self.student_class,
                self.stream,
                self.section
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

            return None

    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear_content()
        self.activate_nav("Dashboard")

        self.header_title.config(
            text="Dashboard"
        )

        df = self.get_data()

        total = 0
        passed = 0
        failed = 0
        pass_percentage = 0
        average = 0
        highest = 0

        if df is not None and not df.empty:

            total = len(df)

            passed = len(
                df[
                    df["Result"] == "PASS"
                ]
            )

            failed = total - passed

            if total:

                pass_percentage = (
                    passed / total * 100
                )

            average = df[
                "Best 5 Percentage"
            ].mean()

            highest = df[
                "Best 5 Percentage"
            ].max()

        tk.Label(
            self.content,
            text="Welcome to the Result Dashboard",
            font=("Segoe UI Semibold", 19),
            fg=DARK,
            bg=BG
        ).pack(
            anchor="w",
            pady=(0, 20)
        )

        cards = tk.Frame(
            self.content,
            bg=BG
        )

        cards.pack(
            fill="x"
        )

        self.stat_card(
            cards,
            "Total Students",
            total,
            BLUE
        )

        self.stat_card(
            cards,
            "Passed",
            passed,
            GREEN
        )

        self.stat_card(
            cards,
            "Failed",
            failed,
            RED
        )

        self.stat_card(
            cards,
            "Pass Percentage",
            f"{pass_percentage:.1f}%",
            PURPLE
        )

        extra = tk.Frame(
            self.content,
            bg=BG
        )

        extra.pack(
            fill="x",
            pady=20
        )

        self.small_card(
            extra,
            "Average Best 5 %",
            f"{average:.2f}%"
        )

        self.small_card(
            extra,
            "Highest Best 5 %",
            f"{highest:.2f}%"
        )

        self.small_card(
            extra,
            "Database",
            "SQLite"
        )

        actions = tk.Frame(
            self.content,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        actions.pack(
            fill="x",
            pady=5
        )

        tk.Label(
            actions,
            text="Quick Actions",
            font=("Segoe UI Semibold", 13),
            fg=DARK,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 12)
        )

        buttons = tk.Frame(
            actions,
            bg=WHITE
        )

        buttons.pack(
            padx=20,
            pady=(0, 20)
        )

        self.action_button(
            buttons,
            "Add Student",
            self.add_student
        )

        self.action_button(
            buttons,
            "View Students",
            self.show_students
        )

        self.action_button(
            buttons,
            "Search",
            self.search_student
        )

        self.action_button(
            buttons,
            "Statistics",
            self.show_statistics
        )

    # ========================================================
    # STAT CARD
    # ========================================================

    def stat_card(
        self,
        parent,
        title,
        value,
        accent
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        tk.Frame(
            card,
            bg=accent,
            width=5
        ).pack(
            side="left",
            fill="y"
        )

        inner = tk.Frame(
            card,
            bg=WHITE
        )

        inner.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=12
        )

        tk.Label(
            inner,
            text=title,
            font=("Segoe UI", 10),
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            inner,
            text=str(value),
            font=("Segoe UI Bold", 24),
            fg=DARK,
            bg=WHITE
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

    # ========================================================
    # SMALL CARD
    # ========================================================

    def small_card(
        self,
        parent,
        title,
        value
    ):

        frame = tk.Frame(
            parent,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        tk.Label(
            frame,
            text=title,
            font=("Segoe UI", 9),
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=15,
            pady=(12, 2)
        )

        tk.Label(
            frame,
            text=value,
            font=("Segoe UI Semibold", 15),
            fg=DARK,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 12)
        )

    # ========================================================
    # ACTION BUTTON
    # ========================================================

    def action_button(
        self,
        parent,
        text,
        command
    ):

        tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI Semibold", 10),
            fg="white",
            bg=BLUE,
            activebackground=BLUE_DARK,
            relief="flat",
            padx=18,
            pady=9,
            cursor="hand2"
        ).pack(
            side="left",
            padx=(0, 10)
        )

    # ========================================================
    # STUDENTS
    # ========================================================

    def show_students(self):

        self.clear_content()
        self.activate_nav("Students")

        self.header_title.config(
            text="Students"
        )

        df = self.get_data()

        toolbar = tk.Frame(
            self.content,
            bg=BG
        )

        toolbar.pack(
            fill="x",
            pady=(0, 15)
        )

        tk.Label(
            toolbar,
            text="Student Records",
            font=("Segoe UI Semibold", 19),
            fg=DARK,
            bg=BG
        ).pack(
            side="left"
        )

        self.action_button(
            toolbar,
            "Add Student",
            self.add_student
        )

        table_frame = tk.Frame(
            self.content,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

        if df is None or df.empty:

            tk.Label(
                table_frame,
                text="No students found.",
                font=("Segoe UI", 13),
                fg=GRAY,
                bg=WHITE
            ).pack(
                expand=True
            )

            return

        columns = list(df.columns)

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        vertical = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        horizontal = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=tree.xview
        )

        tree.configure(
            yscrollcommand=vertical.set,
            xscrollcommand=horizontal.set
        )

        vertical.pack(
            side="right",
            fill="y"
        )

        horizontal.pack(
            side="bottom",
            fill="x"
        )

        tree.pack(
            fill="both",
            expand=True
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            width = 125

            if column == "Student Name":
                width = 160

            if column == "Roll Number":
                width = 90

            tree.column(
                column,
                width=width,
                anchor="center"
            )

        for _, row in df.iterrows():

            values = []

            for column in columns:

                value = row[column]

                if column in (
                    "Overall Percentage",
                    "Best 5 Percentage"
                ):

                    try:
                        value = (
                            f"{float(value):.2f}"
                        )
                    except Exception:
                        pass

                values.append(value)

            tree.insert(
                "",
                "end",
                values=values
            )

        button_bar = tk.Frame(
            self.content,
            bg=BG
        )

        button_bar.pack(
            fill="x",
            pady=(12, 0)
        )

        def selected_student():

            selection = tree.selection()

            if not selection:

                messagebox.showwarning(
                    "Select Student",
                    "Please select a student first."
                )

                return None

            values = tree.item(
                selection[0],
                "values"
            )

            return str(
                values[
                    columns.index("Roll Number")
                ]
            )

        tk.Button(
            button_bar,
            text="Edit Selected",
            command=lambda: self.edit_student(
                selected_student()
            ),
            bg=BLUE,
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            button_bar,
            text="Delete Selected",
            command=lambda: self.delete_student_gui(
                selected_student()
            ),
            bg=RED,
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

    # ========================================================
    # STUDENT FORM
    # ========================================================

    def student_form(
        self,
        title,
        existing=None,
        old_roll=None
    ):

        self.clear_content()

        self.header_title.config(
            text=title
        )

        tk.Label(
            self.content,
            text=title,
            font=("Segoe UI Semibold", 19),
            fg=DARK,
            bg=BG
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        outer = tk.Frame(
            self.content,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        outer.pack(
            fill="both",
            expand=True
        )

        canvas = tk.Canvas(
            outer,
            bg=WHITE,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            outer,
            orient="vertical",
            command=canvas.yview
        )

        form = tk.Frame(
            canvas,
            bg=WHITE
        )

        canvas.create_window(
            (0, 0),
            window=form,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        form.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        # ----------------------------------------------------
        # BASIC DETAILS
        # ----------------------------------------------------

        basic = tk.Frame(
            form,
            bg=WHITE
        )

        basic.pack(
            fill="x",
            padx=30,
            pady=25
        )

        tk.Label(
            basic,
            text="Student Details",
            font=("Segoe UI Semibold", 14),
            fg=DARK,
            bg=WHITE
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(0, 15)
        )

        tk.Label(
            basic,
            text="Roll Number",
            bg=WHITE,
            fg=GRAY
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=8
        )

        roll_entry = tk.Entry(
            basic,
            font=("Segoe UI", 10),
            width=35
        )

        roll_entry.grid(
            row=1,
            column=1,
            padx=20
        )

        tk.Label(
            basic,
            text="Student Name",
            bg=WHITE,
            fg=GRAY
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=8
        )

        name_entry = tk.Entry(
            basic,
            font=("Segoe UI", 10),
            width=35
        )

        name_entry.grid(
            row=2,
            column=1,
            padx=20
        )

        if existing:

            roll_entry.insert(
                0,
                str(existing["Roll Number"])
            )

            name_entry.insert(
                0,
                str(existing["Student Name"])
            )

        # ----------------------------------------------------
        # MARKS
        # ----------------------------------------------------

        tk.Label(
            form,
            text="Subject Marks",
            font=("Segoe UI Semibold", 14),
            fg=DARK,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30,
            pady=(10, 10)
        )

        marks_frame = tk.Frame(
            form,
            bg=WHITE
        )

        marks_frame.pack(
            fill="x",
            padx=30
        )

        mark_entries = {}

        for index, subject in enumerate(
            self.subjects
        ):

            row = index // 2
            col = index % 2

            cell = tk.Frame(
                marks_frame,
                bg="#F8FAFC",
                bd=1,
                relief="solid"
            )

            cell.grid(
                row=row,
                column=col,
                sticky="ew",
                padx=6,
                pady=6
            )

            marks_frame.grid_columnconfigure(
                col,
                weight=1
            )

            tk.Label(
                cell,
                text=subject,
                font=("Segoe UI Semibold", 10),
                fg=DARK,
                bg="#F8FAFC"
            ).pack(
                side="left",
                padx=12,
                pady=12
            )

            entry = tk.Entry(
                cell,
                width=10,
                font=("Segoe UI", 10)
            )

            entry.pack(
                side="right",
                padx=12
            )

            if existing and subject in existing:

                entry.insert(
                    0,
                    str(existing[subject])
                )

            mark_entries[subject] = entry

        # ----------------------------------------------------
        # SAVE
        # ----------------------------------------------------

        def save_student():

            roll = roll_entry.get().strip()
            name = name_entry.get().strip()

            if not roll:

                messagebox.showwarning(
                    "Invalid Roll Number",
                    "Roll number is required."
                )

                return

            if not roll.isalnum():

                messagebox.showwarning(
                    "Invalid Roll Number",
                    "Roll number must contain only letters and numbers."
                )

                return

            if not name:

                messagebox.showwarning(
                    "Invalid Name",
                    "Student name is required."
                )

                return

            if not all(
                character.isalpha() or character.isspace()
                for character in name
            ):

                messagebox.showwarning(
                    "Invalid Name",
                    "Student name must contain letters and spaces only."
                )

                return

            marks = {}

            for subject, entry in mark_entries.items():

                value = entry.get().strip()

                if not value:

                    messagebox.showwarning(
                        "Marks Required",
                        f"Enter marks for {subject}."
                    )

                    return

                try:

                    mark = int(value)

                except ValueError:

                    messagebox.showwarning(
                        "Invalid Marks",
                        f"{subject} marks must be a whole number."
                    )

                    return

                if mark < 0 or mark > 100:

                    messagebox.showwarning(
                        "Invalid Marks",
                        f"{subject} marks must be between 0 and 100."
                    )

                    return

                marks[subject] = mark

            # ------------------------------------------------
            # CALCULATIONS
            # ------------------------------------------------

            result = calculate_complete_result(
                marks
            )

            student = {
                "Roll Number": roll,
                "Student Name": name
            }

            student.update(
                marks
            )

            student.update(
                result
            )

            # ------------------------------------------------
            # UPDATE
            # ------------------------------------------------

            if existing:

                success = update_student(
                    self.academic_year,
                    self.student_class,
                    self.stream,
                    self.section,
                    old_roll,
                    student
                )

                if success:

                    messagebox.showinfo(
                        "Success",
                        "Student updated successfully."
                    )

                    self.show_students()

                else:

                    messagebox.showerror(
                        "Update Failed",
                        "Could not update the student."
                    )

            # ------------------------------------------------
            # INSERT
            # ------------------------------------------------

            else:

                df = self.get_data()

                if df is not None and not df.empty:

                    existing_rolls = set(
                        df["Roll Number"]
                        .astype(str)
                    )

                    if roll in existing_rolls:

                        messagebox.showwarning(
                            "Duplicate Roll Number",
                            "This roll number already exists."
                        )

                        return

                success = insert_student_record(
                    self.academic_year,
                    self.student_class,
                    self.stream,
                    self.section,
                    student
                )

                if success:

                    messagebox.showinfo(
                        "Success",
                        "Student added successfully."
                    )

                    self.show_students()

                else:

                    messagebox.showerror(
                        "Save Failed",
                        "Could not save the student."
                    )

        button_bar = tk.Frame(
            form,
            bg=WHITE
        )

        button_bar.pack(
            fill="x",
            padx=30,
            pady=25
        )

        tk.Button(
            button_bar,
            text="Save Student",
            command=save_student,
            bg=GREEN,
            fg="white",
            activebackground="#15803D",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(
            side="left",
            padx=(0, 10)
        )

        tk.Button(
            button_bar,
            text="Cancel",
            command=self.show_students,
            bg="#6B7280",
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(
            side="left"
        )

    # ========================================================
    # ADD
    # ========================================================

    def add_student(self):

        self.activate_nav(
            "Add Student"
        )

        self.student_form(
            "Add New Student"
        )

    # ========================================================
    # EDIT
    # ========================================================

    def edit_student(
        self,
        roll_number
    ):

        if not roll_number:

            return

        df = self.get_data()

        if df is None or df.empty:

            return

        matches = df[
            df["Roll Number"]
            .astype(str)
            ==
            str(roll_number)
        ]

        if matches.empty:

            messagebox.showerror(
                "Not Found",
                "Student not found."
            )

            return

        student = matches.iloc[0].to_dict()

        self.activate_nav(
            "Students"
        )

        self.student_form(
            "Edit Student",
            existing=student,
            old_roll=str(roll_number)
        )

    # ========================================================
    # DELETE
    # ========================================================

    def delete_student_gui(
        self,
        roll_number
    ):

        if not roll_number:

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            f"Delete student with Roll Number {roll_number}?"
        )

        if not answer:

            return

        success = delete_student(
            self.academic_year,
            self.student_class,
            self.stream,
            self.section,
            roll_number
        )

        if success:

            messagebox.showinfo(
                "Deleted",
                "Student deleted successfully."
            )

            self.show_students()

        else:

            messagebox.showerror(
                "Delete Failed",
                "Student could not be deleted."
            )

    # ========================================================
    # SEARCH
    # ========================================================

    def search_student(self):

        self.clear_content()

        self.activate_nav(
            "Search Student"
        )

        self.header_title.config(
            text="Search Student"
        )

        tk.Label(
            self.content,
            text="Search Student",
            font=("Segoe UI Semibold", 19),
            fg=DARK,
            bg=BG
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        search_bar = tk.Frame(
            self.content,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        search_bar.pack(
            fill="x",
            pady=(0, 15)
        )

        entry = tk.Entry(
            search_bar,
            font=("Segoe UI", 11),
            width=40
        )

        entry.pack(
            side="left",
            padx=20,
            pady=18
        )

        result_frame = tk.Frame(
            self.content,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        result_frame.pack(
            fill="both",
            expand=True
        )

        def perform_search():

            for widget in result_frame.winfo_children():

                widget.destroy()

            query = (
                entry.get()
                .strip()
                .lower()
            )

            if not query:

                return

            df = self.get_data()

            if df is None or df.empty:

                return

            matches = df[
                df["Roll Number"]
                .astype(str)
                .str.lower()
                .str.contains(
                    query,
                    na=False
                )
                |
                df["Student Name"]
                .astype(str)
                .str.lower()
                .str.contains(
                    query,
                    na=False
                )
            ]

            if matches.empty:

                tk.Label(
                    result_frame,
                    text="No matching student found.",
                    font=("Segoe UI", 12),
                    fg=GRAY,
                    bg=WHITE
                ).pack(
                    expand=True
                )

                return

            self.create_tree(
                result_frame,
                matches
            )

        tk.Button(
            search_bar,
            text="Search",
            command=perform_search,
            bg=BLUE,
            fg="white",
            relief="flat",
            padx=20,
            pady=8
        ).pack(
            side="left"
        )

        entry.bind(
            "<Return>",
            lambda event: perform_search()
        )

    # ========================================================
    # TREEVIEW HELPER
    # ========================================================

    def create_tree(
        self,
        parent,
        df
    ):

        columns = list(
            df.columns
        )

        tree = ttk.Treeview(
            parent,
            columns=columns,
            show="headings"
        )

        scroll_y = ttk.Scrollbar(
            parent,
            orient="vertical",
            command=tree.yview
        )

        scroll_x = ttk.Scrollbar(
            parent,
            orient="horizontal",
            command=tree.xview
        )

        tree.configure(
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.pack(
            side="right",
            fill="y"
        )

        scroll_x.pack(
            side="bottom",
            fill="x"
        )

        tree.pack(
            fill="both",
            expand=True
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=120,
                anchor="center"
            )

        for _, row in df.iterrows():

            values = []

            for column in columns:

                value = row[column]

                if column in (
                    "Overall Percentage",
                    "Best 5 Percentage"
                ):

                    try:

                        value = (
                            f"{float(value):.2f}"
                        )

                    except Exception:

                        pass

                values.append(
                    value
                )

            tree.insert(
                "",
                "end",
                values=values
            )

        return tree

    # ========================================================
    # TOPPER
    # ========================================================

    def show_topper(self):

        self.clear_content()

        self.activate_nav(
            "Topper"
        )

        self.header_title.config(
            text="Topper"
        )

        df = self.get_data()

        if df is None or df.empty:

            self.show_empty(
                "No student data available."
            )

            return

        highest = df[
            "Best 5 Percentage"
        ].max()

        toppers = df[
            df["Best 5 Percentage"]
            ==
            highest
        ]

        tk.Label(
            self.content,
            text="Top Student(s)",
            font=("Segoe UI Semibold", 19),
            fg=DARK,
            bg=BG
        ).pack(
            anchor="w",
            pady=(0, 20)
        )

        for _, student in toppers.iterrows():

            card = tk.Frame(
                self.content,
                bg=WHITE,
                bd=1,
                relief="solid"
            )

            card.pack(
                fill="x",
                pady=5
            )

            tk.Label(
                card,
                text="🏆",
                font=("Segoe UI", 28),
                bg=WHITE
            ).pack(
                side="left",
                padx=20,
                pady=15
            )

            info = tk.Frame(
                card,
                bg=WHITE
            )

            info.pack(
                side="left"
            )

            tk.Label(
                info,
                text=str(
                    student["Student Name"]
                ),
                font=("Segoe UI Semibold", 15),
                fg=DARK,
                bg=WHITE
            ).pack(
                anchor="w"
            )

            tk.Label(
                info,
                text=(
                    f"Roll Number: "
                    f"{student['Roll Number']}"
                ),
                fg=GRAY,
                bg=WHITE
            ).pack(
                anchor="w"
            )

            tk.Label(
                card,
                text=f"{highest:.2f}%",
                font=("Segoe UI Bold", 22),
                fg=GREEN,
                bg=WHITE
            ).pack(
                side="right",
                padx=30
            )

    # ========================================================
    # STATISTICS
    # ========================================================

    def show_statistics(self):

        self.clear_content()

        self.activate_nav(
            "Statistics"
        )

        self.header_title.config(
            text="Statistics"
        )

        df = self.get_data()

        if df is None or df.empty:

            self.show_empty(
                "No student data available."
            )

            return

        total = len(df)

        passed = len(
            df[
                df["Result"] == "PASS"
            ]
        )

        failed = total - passed

        pass_percentage = (
            passed / total * 100
            if total
            else 0
        )

        average = df[
            "Best 5 Percentage"
        ].mean()

        highest = df[
            "Best 5 Percentage"
        ].max()

        lowest = df[
            "Best 5 Percentage"
        ].min()

        cards = tk.Frame(
            self.content,
            bg=BG
        )

        cards.pack(
            fill="x"
        )

        self.stat_card(
            cards,
            "Students",
            total,
            BLUE
        )

        self.stat_card(
            cards,
            "Passed",
            passed,
            GREEN
        )

        self.stat_card(
            cards,
            "Failed",
            failed,
            RED
        )

        self.stat_card(
            cards,
            "Pass %",
            f"{pass_percentage:.2f}%",
            PURPLE
        )

        detail = tk.Frame(
            self.content,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        detail.pack(
            fill="x",
            pady=25
        )

        values = [
            ("Average Best 5 Percentage", average),
            ("Highest Best 5 Percentage", highest),
            ("Lowest Best 5 Percentage", lowest)
        ]

        for label, value in values:

            row = tk.Frame(
                detail,
                bg=WHITE
            )

            row.pack(
                fill="x",
                padx=25,
                pady=10
            )

            tk.Label(
                row,
                text=label,
                fg=GRAY,
                bg=WHITE
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=f"{value:.2f}%",
                font=("Segoe UI Semibold", 10),
                fg=DARK,
                bg=WHITE
            ).pack(
                side="right"
            )

    # ========================================================
    # GRAPHS
    # ========================================================

    def show_graphs(self):

        self.clear_content()

        self.activate_nav(
            "Graphs"
        )

        self.header_title.config(
            text="Graphs"
        )

        tk.Label(
            self.content,
            text="Result Graphs",
            font=("Segoe UI Semibold", 19),
            fg=DARK,
            bg=BG
        ).pack(
            anchor="w",
            pady=(0, 20)
        )

        tk.Button(
            self.content,
            text="Best 5 Percentage Graph",
            command=self.best5_graph,
            bg=BLUE,
            fg="white",
            relief="flat",
            padx=20,
            pady=10
        ).pack(
            anchor="w",
            pady=5
        )

        tk.Button(
            self.content,
            text="Subject Marks Graph",
            command=self.subject_graph,
            bg=PURPLE,
            fg="white",
            relief="flat",
            padx=20,
            pady=10
        ).pack(
            anchor="w",
            pady=5
        )

        tk.Label(
            self.content,
            text="Graphs are saved inside the exports folder.",
            fg=GRAY,
            bg=BG
        ).pack(
            anchor="w",
            pady=15
        )

    def best5_graph(self):

        try:

            from modules.graphs import (
                show_best_5_percentage_graph
            )

            df = self.get_data()

            if df is None or df.empty:

                messagebox.showwarning(
                    "No Data",
                    "No students available."
                )

                return

            path = show_best_5_percentage_graph(
                df
            )

            messagebox.showinfo(
                "Graph Created",
                f"Saved:\n{path}"
            )

        except Exception as error:

            messagebox.showerror(
                "Graph Error",
                str(error)
            )

    def subject_graph(self):

        df = self.get_data()

        if df is None or df.empty:

            messagebox.showwarning(
                "No Data",
                "No students available."
            )

            return

        subject_window = tk.Toplevel(
            self.root
        )

        subject_window.title(
            "Select Subject"
        )

        subject_window.geometry(
            "350x200"
        )

        tk.Label(
            subject_window,
            text="Select Subject",
            font=("Segoe UI Semibold", 13)
        ).pack(
            pady=20
        )

        subject_var = tk.StringVar()

        combo = ttk.Combobox(
            subject_window,
            textvariable=subject_var,
            values=self.subjects,
            state="readonly",
            width=28
        )

        combo.pack()

        combo.current(0)

        def generate():

            try:

                from modules.graphs import (
                    show_subject_marks_graph
                )

                path = show_subject_marks_graph(
                    df,
                    subject_var.get()
                )

                subject_window.destroy()

                messagebox.showinfo(
                    "Graph Created",
                    f"Saved:\n{path}"
                )

            except Exception as error:

                messagebox.showerror(
                    "Graph Error",
                    str(error)
                )

        tk.Button(
            subject_window,
            text="Generate",
            command=generate,
            bg=BLUE,
            fg="white",
            relief="flat",
            padx=20,
            pady=8
        ).pack(
            pady=20
        )

    # ========================================================
    # EXPORT
    # ========================================================

    def export_result(self):

        self.clear_content()

        self.activate_nav(
            "Export Result"
        )

        self.header_title.config(
            text="Export Result"
        )

        tk.Label(
            self.content,
            text="Export Result Sheet",
            font=("Segoe UI Semibold", 19),
            fg=DARK,
            bg=BG
        ).pack(
            anchor="w",
            pady=(0, 20)
        )

        tk.Button(
            self.content,
            text="Export CSV",
            command=self.perform_export,
            bg=BLUE,
            fg="white",
            relief="flat",
            padx=25,
            pady=10
        ).pack(
            anchor="w"
        )

    def perform_export(self):

        try:

            from modules.export import (
                export_result_sheet
            )

            df = self.get_data()

            if df is None or df.empty:

                messagebox.showwarning(
                    "No Data",
                    "No students available for export."
                )

                return

            path = export_result_sheet(
                df,
                self.academic_year,
                self.student_class,
                self.stream,
                self.section
            )

            messagebox.showinfo(
                "Export Complete",
                f"Result exported successfully.\n\n{path}"
            )

        except Exception as error:

            messagebox.showerror(
                "Export Error",
                str(error)
            )

    # ========================================================
    # SETTINGS
    # ========================================================

    def show_settings(self):

        self.clear_content()

        self.activate_nav(
            "Settings"
        )

        self.header_title.config(
            text="Settings"
        )

        tk.Label(
            self.content,
            text="Current Configuration",
            font=("Segoe UI Semibold", 19),
            fg=DARK,
            bg=BG
        ).pack(
            anchor="w",
            pady=(0, 20)
        )

        card = tk.Frame(
            self.content,
            bg=WHITE,
            bd=1,
            relief="solid"
        )

        card.pack(
            fill="x"
        )

        settings = [
            ("Academic Year", self.academic_year),
            ("Class", f"Class {self.student_class}"),
            ("Stream", self.stream or "Not Applicable"),
            ("Language", self.language),
            ("Science Choice", self.science_choice),
            ("Optional Subject", self.optional_subject),
            ("Section", self.section),
            ("Database", "SQLite")
        ]

        for label, value in settings:

            row = tk.Frame(
                card,
                bg=WHITE
            )

            row.pack(
                fill="x",
                padx=25,
                pady=10
            )

            tk.Label(
                row,
                text=label,
                fg=GRAY,
                bg=WHITE
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=value,
                font=("Segoe UI Semibold", 10),
                fg=DARK,
                bg=WHITE
            ).pack(
                side="right"
            )

        tk.Button(
            self.content,
            text="Restart / Change Configuration",
            command=self.restart_configuration,
            bg=BLUE,
            fg="white",
            relief="flat",
            padx=20,
            pady=10
        ).pack(
            anchor="w",
            pady=20
        )

    # ========================================================
    # RESTART CONFIGURATION
    # ========================================================

    def restart_configuration(self):

        self.root.destroy()

        import subprocess

        subprocess.Popen(
            [
                sys.executable,
                os.path.join(
                    PROJECT_ROOT,
                    "run.py"
                )
            ]
        )

    # ========================================================
    # EMPTY PAGE
    # ========================================================

    def show_empty(
        self,
        message
    ):

        frame = tk.Frame(
            self.content,
            bg=WHITE
        )

        frame.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            frame,
            text=message,
            font=("Segoe UI", 13),
            fg=GRAY,
            bg=WHITE
        ).pack(
            expand=True
        )


# ============================================================
# START GUI
# ============================================================

def start_gui(
    academic_year,
    student_class,
    stream,
    section,
    language="English",
    science_choice="Mathematics",
    optional_subject="None"
):

    root = tk.Tk()

    SchoolResultGUI(
        root,
        academic_year,
        student_class,
        stream,
        section,
        language,
        science_choice,
        optional_subject
    )

    root.mainloop()


# ============================================================
# DIRECT TEST
# ============================================================

if __name__ == "__main__":

    start_gui(
        "2026-27",
        9,
        None,
        "A"
    )