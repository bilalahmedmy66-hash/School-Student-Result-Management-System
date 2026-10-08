\# School Student Result Management System



A complete Python-based School Student Result Management System for Classes 9 to 12.



The system provides a graphical interface using Tkinter and stores student records using SQLite.



\## Features



\- Academic Year configuration

\- Class 9, 10, 11 and 12 support

\- Section management

\- Science, Commerce and Arts/Humanities streams

\- English/Hindi language selection

\- Mathematics/Biology selection for Science

\- Optional subjects for Classes 9 and 10

\- Add students

\- View all students

\- Search students

\- Edit student records

\- Delete student records

\- Automatic total marks calculation

\- Overall percentage calculation

\- Best 5 calculation

\- Best 5 percentage

\- Automatic PASS/FAIL result

\- Topper detection

\- Statistics

\- Pass percentage

\- Average performance

\- Highest and lowest performance

\- Matplotlib graphs

\- CSV result export

\- SQLite database

\- Tkinter GUI

\- Input validation

\- Configuration restart



\## Technologies Used



\- Python

\- Tkinter

\- SQLite

\- Pandas

\- Matplotlib

\- CSV

\- JSON

\- OS

\- Regular Expressions



\## Project Structure



```text

School\_Result\_Management\_System/

│

├── run.py

├── main.py

├── config.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── database/

│   └── school.db

│

├── school\_data/

│

├── exports/

│

├── gui/

│   ├── \_\_init\_\_.py

│   └── main\_window.py

│

├── modules/

│   ├── \_\_init\_\_.py

│   ├── subjects.py

│   ├── validation.py

│   ├── calculations.py

│   ├── csv\_manager.py

│   ├── database.py

│   ├── student\_manager.py

│   ├── search.py

│   ├── topper.py

│   ├── statistics.py

│   ├── graphs.py

│   └── export.py

│

└── tests/

