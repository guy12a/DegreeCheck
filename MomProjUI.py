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

    def getName(self):
        return self.name_input.text()

    def getDate(self):
        return self.start_date_input.text()

class MandatorySection(QWidget):
    def __init__(self,mandCourses):
        super().__init__()

        label = QLabel("קורסי חובה")
        label.setAlignment(Qt.AlignCenter)

        self.course1 = HebCheckbox(mandCourses[0])
        self.course2 = HebCheckbox(mandCourses[1])
        self.course3 = HebCheckbox(mandCourses[2])
        self.course4 = HebCheckbox(mandCourses[3])

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.course1)
        layout.addWidget(self.course2)
        layout.addWidget(self.course3)
        layout.addWidget(self.course4)

        self.setLayout(layout)

    def getChecked(self):
        checkedCourses = []
        if self.course1.isChecked():
            checkedCourses.append(0)
        if self.course2.isChecked():
            checkedCourses.append(1)
        if self.course3.isChecked():
            checkedCourses.append(2)
        if self.course4.isChecked():
            checkedCourses.append(3)
        return checkedCourses

    def getCredMandatory(self):
        counter = 0
        if self.course1.isChecked():
            counter+=1
        if self.course2.isChecked():
            counter+=1
        if self.course3.isChecked():
            counter+=1
        if self.course4.isChecked():
            counter+=1
        return counter*2

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

    def getSeminar(self):
        if self.semi1.isChecked():
            return 1
        elif self.semi2.isChecked():
            return 2
        else:
            return 0

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

    def getElectives(self):
        electives = []
        for line in self.electiveLines:
            if line.getCourseName() != "" and line.getCredits() != "":
                electives.append((line.getCourseName(),line.getCredits()))

        return electives

    def getElectiveCredit(self):
        sum = 0
        for line in self.electiveLines:
            if line.getCourseName() != "" and line.getCredits() != "":
                sum += int (line.getCredits())
        return sum


class ElectiveLine(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        self.course_name = QLineEdit(placeholderText="שם הקורס")
        self.credits = QLineEdit(placeholderText="נק״ז")

        layout.addWidget(self.credits, 1)
        layout.addWidget(self.course_name, 5)


        self.setLayout(layout)

    def getCourseName(self):
        return self.course_name.text()

    def getCredits(self):
        return self.credits.text()


class HebCheckbox(QCheckBox):
    def __init__(self,text):
        super().__init__(text)
        self.setLayoutDirection(Qt.RightToLeft)

class HebRadio(QRadioButton):
    def __init__(self,text):
        super().__init__(text)
        self.setLayoutDirection(Qt.RightToLeft)