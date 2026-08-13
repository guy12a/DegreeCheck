from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QRadioButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mom's App")
        #self.setFixedSize(QSize(500,400)) #can also use setMinimumSize or setMaximumSize

        layout = QVBoxLayout()
        layout.addWidget(PersonalDetailsSection())
        layout.addWidget(MandatorySection())
        layout.addWidget(SeminarSection())


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class PersonalDetailsSection(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("פרטים אישיים")
        label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(QLineEdit(placeholderText="הכניסי את שם הסטודנט"))
        layout.addWidget(QLineEdit(placeholderText="הכניסי תאריך תחילת לימודים בחטיבה"))

        
        self.setLayout(layout)

class SeminarSection(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("סמינרים")
        label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(HebRadio("ללא"))
        layout.addWidget(HebRadio("התמודדות מתבגרים במצבי קונפליקט"))
        layout.addWidget(HebRadio("קונפליקטים במרחב המשפחתי"))

        self.setLayout(layout)

class MandatorySection(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("קורסי חובה")
        label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(HebCheckbox("מושגי יסוד בחקר סכסוכים"))
        layout.addWidget(HebCheckbox("מבנה חברתי של ישראל"))
        layout.addWidget(HebCheckbox("סוגיות בקונפליקטים קבוצתיים וארגוניים"))
        layout.addWidget(HebCheckbox("משא ומתן ככלי לניהול וישוב סכסוכים"))

        self.setLayout(layout)


class HebCheckbox(QCheckBox):
    def __init__(self,text):
        super().__init__(text)
        self.setLayoutDirection(Qt.RightToLeft)

class HebRadio(QRadioButton):
    def __init__(self,text):
        super().__init__(text)
        self.setLayoutDirection(Qt.RightToLeft)



app = QApplication([]) #manages event loop

window = MainWindow() #manages the UI - holds all other widgets
window.show()

app.exec()