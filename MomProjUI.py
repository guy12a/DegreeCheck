from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QRadioButton, QVBoxLayout, QWidget


class PersonalDetailsSection(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("פרטים אישיים")
        label.setAlignment(Qt.AlignCenter)

        self.name_input = QLineEdit(placeholderText="הכניסי את שם הסטודנט")
        self.start_date_input = QLineEdit(placeholderText="הכניסי תאריך תחילת לימודים בחטיבה")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.start_date_input)

        
        self.setLayout(layout)

class MandatorySection(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("קורסי חובה")
        label.setAlignment(Qt.AlignCenter)

        self.course1 = HebCheckbox("מושגי יסוד בחקר סכסוכים")
        self.course2 = HebCheckbox("מבנה חברתי של ישראל")
        self.course3 = HebCheckbox("סוגיות בקונפליקטים קבוצתיים וארגוניים")
        self.course4 = HebCheckbox("משא ומתן ככלי לניהול וישוב סכסוכים")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.course1)
        layout.addWidget(self.course2)
        layout.addWidget(self.course3)
        layout.addWidget(self.course4)

        self.setLayout(layout)

class SeminarSection(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("סמינרים")
        label.setAlignment(Qt.AlignCenter)

        self.noSemi = HebRadio("ללא")
        self.semi1 = HebRadio("התמודדות מתבגרים במצבי קונפליקט")
        self.semi2 = HebRadio("קונפליקטים במרחב המשפחתי")


        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.noSemi)
        layout.addWidget(self.semi1)
        layout.addWidget(self.semi2)

        self.setLayout(layout)

class ElectivesSection(QWidget):
    def __init__(self, text, num):
        super().__init__()

        label = QLabel(text=text)
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("הוסיפי שורה")
        button.clicked.connect(self.addRowClick)

        self.electiveLines = []

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(button)
        for i in range(num):
            self.addRowClick()



        self.setLayout(self.main_layout)

    def addRowClick(self):
        row = ElectiveLine()
        self.electiveLines.append(row)
        self.main_layout.insertWidget(self.main_layout.count() - 1, row)

class ElectiveLine(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        course_name = QLineEdit(placeholderText="שם הקורס")
        credits = QLineEdit(placeholderText="נק״ז")

        layout.addWidget(credits, 1)
        layout.addWidget(course_name, 5)


        self.setLayout(layout)


class HebCheckbox(QCheckBox):
    def __init__(self,text):
        super().__init__(text)
        self.setLayoutDirection(Qt.RightToLeft)

class HebRadio(QRadioButton):
    def __init__(self,text):
        super().__init__(text)
        self.setLayoutDirection(Qt.RightToLeft)