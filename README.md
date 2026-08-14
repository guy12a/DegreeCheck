# Mom's App

A Python desktop application for managing and checking course requirements for the **Conflict Management and Resolution** track.

The application provides a simple Hebrew/RTL graphical interface where users can enter student details, select mandatory courses and seminars, add elective courses, and generate a formatted Word document summarizing the student's requirements.

## Features

* Hebrew / RTL user interface
* Personal student information entry
* Selection of completed mandatory courses
* Seminar selection
* Dynamically add elective course rows
* Separate internal and external elective courses
* Automatic calculation of elective course credits
* Generates a formatted `.docx` document
* Hebrew-specific Word formatting, including RTL text, fonts, sizes, and bold/underline formatting
* Windows executable available through PyInstaller

## Technologies

* **Python**
* **PySide6** — graphical user interface
* **python-docx** — Word document generation
* **PyInstaller** — application packaging

## Project Structure

```text
.
├── main.py
├── ProjUI.py
├── GenerateDocx.py
└── README.md
```

The application is divided into GUI sections, with each section responsible for its own inputs and data retrieval. The collected information is then passed to the DOCX generation code.

## Running from Source

Make sure Python is installed, then install the required dependencies:

```bash
pip install PySide6 python-docx
```

Run the application with:

```bash
python main.py
```

## Building the Executable

The application can be packaged into a standalone Windows executable using PyInstaller:

```bash
python -m PyInstaller --onefile --windowed main.py
```

The resulting executable will be placed in:

```text
dist/
```

The executable can be run on a Windows computer without requiring Python to be installed.

## Usage

1. Enter the student's personal details.
2. Select the completed mandatory courses.
3. Select the applicable seminar.
4. Enter internal elective courses and their credits.
5. Enter elective courses taken from other departments, if applicable.
6. Click **"שמירה לקובץ וורד"** to generate the Word document.
7. The generated document contains a formatted summary of the student's completed requirements.

## Notes

The application is designed primarily for Hebrew-language use. Special handling is used when generating the Word document because Hebrew is treated as a complex/RTL script by Microsoft Word. This includes explicit handling of RTL direction, complex-script fonts, font sizes, and bold formatting.

## License

This project is currently intended for personal/internal use.
