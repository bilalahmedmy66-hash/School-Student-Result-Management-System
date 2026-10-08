import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(
        0,
        PROJECT_ROOT
    )


# ============================================================
# DATABASE
# ============================================================

from modules.database import initialize_database


# ============================================================
# GUI
# ============================================================

from gui.main_window import start_gui


# ============================================================
# STARTUP WINDOW
# ============================================================

class StartupWindow:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "School Result Management System"
        )

        self.root.geometry(
            "650x760"
        )

        self.root.resizable(
            False,
            False
        )

        self.root.configure(
            bg="#F4F7FB"
        )

        self.build()

    # ========================================================
    # BUILD
    # ========================================================

    def build(self):

        header = tk.Frame(
            self.root,
            bg="#172033",
            height=130
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="SCHOOL RESULT",
            font=("Segoe UI Bold", 25),
            fg="white",
            bg="#172033"
        ).pack(
            pady=(25, 0)
        )

        tk.Label(
            header,
            text="Student Result Management System",
            font=("Segoe UI", 10),
            fg="#AEB8CA",
            bg="#172033"
        ).pack()

        card = tk.Frame(
            self.root,
            bg="white",
            bd=1,
            relief="solid"
        )

        card.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=25
        )

        tk.Label(
            card,
            text="Configure Your Session",
            font=("Segoe UI Semibold", 18),
            fg="#172033",
            bg="white"
        ).pack(
            pady=(25, 5)
        )

        self.label(
            card,
            "Academic Year"
        )

        self.year = tk.Entry(
            card,
            width=35,
            font=("Segoe UI", 10)
        )

        self.year.pack(
            pady=(0, 12)
        )

        self.year.insert(
            0,
            "2026-27"
        )

        self.label(
            card,
            "Class"
        )

        self.class_var = tk.StringVar()

        self.class_combo = ttk.Combobox(
            card,
            textvariable=self.class_var,
            values=["9", "10", "11", "12"],
            state="readonly",
            width=32
        )

        self.class_combo.pack(
            pady=(0, 12)
        )

        self.class_combo.current(0)

        self.class_combo.bind(
            "<<ComboboxSelected>>",
            self.class_changed
        )

        # ----------------------------------------------------
        # STREAM
        # ----------------------------------------------------

        self.stream_label = self.label(
            card,
            "Stream",
            pack_now=False
        )

        self.stream_var = tk.StringVar()

        self.stream_combo = ttk.Combobox(
            card,
            textvariable=self.stream_var,
            values=[
                "Science",
                "Commerce",
                "Arts/Humanities"
            ],
            state="readonly",
            width=32
        )

        # ----------------------------------------------------
        # LANGUAGE
        # ----------------------------------------------------

        self.language_label = self.label(
            card,
            "Language",
            pack_now=False
        )

        self.language_var = tk.StringVar()

        self.language_combo = ttk.Combobox(
            card,
            textvariable=self.language_var,
            values=[
                "English",
                "Hindi"
            ],
            state="readonly",
            width=32
        )

        self.language_combo.current(0)

        # ----------------------------------------------------
        # SCIENCE CHOICE
        # ----------------------------------------------------

        self.science_label = self.label(
            card,
            "Science Subject",
            pack_now=False
        )

        self.science_var = tk.StringVar()

        self.science_combo = ttk.Combobox(
            card,
            textvariable=self.science_var,
            values=[
                "Mathematics",
                "Biology"
            ],
            state="readonly",
            width=32
        )

        self.science_combo.current(0)

        # ----------------------------------------------------
        # OPTIONAL
        # ----------------------------------------------------

        self.optional_label = self.label(
            card,
            "Optional Subject",
            pack_now=False
        )

        self.optional_var = tk.StringVar()

        self.optional_combo = ttk.Combobox(
            card,
            textvariable=self.optional_var,
            values=[
                "None",
                "Information Technology",
                "Artificial Intelligence",
                "Sanskrit",
                "French",
                "Physical Education",
                "Painting"
            ],
            state="readonly",
            width=32
        )

        self.optional_combo.current(0)

        # ----------------------------------------------------
        # SECTION
        # ----------------------------------------------------

        self.label(
            card,
            "Section"
        )

        self.section_var = tk.StringVar()

        self.section_combo = ttk.Combobox(
            card,
            textvariable=self.section_var,
            values=[
                "A",
                "B",
                "C",
                "D"
            ],
            state="readonly",
            width=32
        )

        self.section_combo.pack(
            pady=(0, 20)
        )

        self.section_combo.current(0)

        # ----------------------------------------------------
        # START
        # ----------------------------------------------------

        tk.Button(
            card,
            text="START SYSTEM",
            command=self.start,
            font=("Segoe UI Semibold", 11),
            fg="white",
            bg="#2563EB",
            activebackground="#1D4ED8",
            relief="flat",
            padx=45,
            pady=12,
            cursor="hand2"
        ).pack(
            pady=5
        )

        tk.Label(
            card,
            text="Python • SQLite • Pandas • Matplotlib • Tkinter",
            font=("Segoe UI", 8),
            fg="#9CA3AF",
            bg="white"
        ).pack(
            pady=(15, 20)
        )

        self.class_changed()

    # ========================================================
    # LABEL
    # ========================================================

    def label(
        self,
        parent,
        text,
        pack_now=True
    ):

        label = tk.Label(
            parent,
            text=text,
            font=("Segoe UI Semibold", 9),
            fg="#374151",
            bg="white"
        )

        if pack_now:

            label.pack(
                anchor="w",
                padx=55
            )

        return label

    # ========================================================
    # CLASS CHANGED
    # ========================================================

    def class_changed(
        self,
        event=None
    ):

        selected = self.class_var.get()

        # Hide all optional fields first

        for widget in [
            self.stream_label,
            self.stream_combo,
            self.language_label,
            self.language_combo,
            self.science_label,
            self.science_combo,
            self.optional_label,
            self.optional_combo
        ]:

            widget.pack_forget()

        if selected in ("9", "10"):

            self.optional_label.pack(
                anchor="w",
                padx=55
            )

            self.optional_combo.pack(
                pady=(0, 12)
            )

        else:

            self.stream_label.pack(
                anchor="w",
                padx=55
            )

            self.stream_combo.pack(
                pady=(0, 12)
            )

            self.language_label.pack(
                anchor="w",
                padx=55
            )

            self.language_combo.pack(
                pady=(0, 12)
            )

            if self.stream_var.get() == "Science":

                self.science_label.pack(
                    anchor="w",
                    padx=55
                )

                self.science_combo.pack(
                    pady=(0, 12)
                )

        # Section remains visible because it was created before
        # the dynamic fields.

    # ========================================================
    # START
    # ========================================================

    def start(self):

        year = self.year.get().strip()
        class_value = self.class_var.get().strip()
        stream = self.stream_var.get().strip()
        language = self.language_var.get().strip()
        science_choice = self.science_var.get().strip()
        optional = self.optional_var.get().strip()
        section = self.section_var.get().strip()

        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if len(year) != 7 or year[4] != "-":

            messagebox.showwarning(
                "Invalid Academic Year",
                "Use format YYYY-YY, for example 2026-27."
            )

            return

        if not class_value:

            messagebox.showwarning(
                "Class Required",
                "Please select a class."
            )

            return

        if class_value in ("11", "12"):

            if not stream:

                messagebox.showwarning(
                    "Stream Required",
                    "Please select a stream."
                )

                return

            if not language:

                messagebox.showwarning(
                    "Language Required",
                    "Please select English or Hindi."
                )

                return

            if stream == "Science" and not science_choice:

                messagebox.showwarning(
                    "Subject Required",
                    "Select Mathematics or Biology."
                )

                return

        if class_value in ("9", "10"):

            if not optional:

                optional = "None"

        student_class = int(
            class_value
        )

        # ----------------------------------------------------
        # CLOSE
        # ----------------------------------------------------

        self.root.destroy()

        # ----------------------------------------------------
        # OPEN MAIN GUI
        # ----------------------------------------------------

        start_gui(
            year,
            student_class,
            stream if student_class >= 11 else None,
            section,
            language,
            science_choice,
            optional
        )


# ============================================================
# MAIN
# ============================================================

def main():

    initialize_database()

    root = tk.Tk()

    StartupWindow(
        root
    )

    root.mainloop()


if __name__ == "__main__":

    main()