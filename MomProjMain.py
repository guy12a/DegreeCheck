from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

from GenerateDocx import constructFile
from MomProjUI import ElectivesSection, MandatorySection, PersonalDetailsSection, SeminarSection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mandatoryCourses = [
            'מושגי יסוד בחקר סכסוכים',
            'מבנה חברתי של ישראל',
            'סוגיות בקונפליקטים קבוצתיים וארגוניים',
            'משא ומתן ככלי לניהול וישוב סכסוכים'
        ]

        self.setWindowTitle("Mom's App")
        self.setMinimumWidth(500)
        #self.setFixedSize(QSize(500,400)) #can also use setMinimumSize or setMaximumSize

        self.details = PersonalDetailsSection()
        self.mandatory = MandatorySection(self.mandatoryCourses)
        self.seminar = SeminarSection()
        self.internalElect = ElectivesSection("קורסי בחירה בחטיבה",3)
        self.externalElect = ElectivesSection("קורסי בחירה ממחלקות אחרות",0)

        button = QPushButton("שמירה לקובץ וורד")
        button.clicked.connect(self.saveButtonClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.details)
        layout.addWidget(self.mandatory)
        layout.addWidget(self.seminar)
        layout.addWidget(self.internalElect)
        layout.addWidget(self.externalElect)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def saveButtonClicked(self):
        constructFile(self.details.getName(),self.details.getDate(),
                      self.mandatory.getChecked(),self.mandatory.getCredMandatory(),self.mandatoryCourses,
                      self.seminar.getSeminar(),
                      self.internalElect.getElectives(),self.externalElect.getElectives(),
                      self.internalElect.getElectiveCredit()+self.externalElect.getElectiveCredit())



app = QApplication([]) #manages event loop

window = MainWindow() #manages the UI - holds all other widgets
window.show()

app.exec()

