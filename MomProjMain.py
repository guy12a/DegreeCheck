from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

from MomProjUI import ElectivesSection, MandatorySection, PersonalDetailsSection, SeminarSection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mom's App")
        self.setMinimumWidth(500)
        #self.setFixedSize(QSize(500,400)) #can also use setMinimumSize or setMaximumSize

        self.details = PersonalDetailsSection()
        self.mandatory = MandatorySection()
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
        pass



app = QApplication([]) #manages event loop

window = MainWindow() #manages the UI - holds all other widgets
window.show()

app.exec()

