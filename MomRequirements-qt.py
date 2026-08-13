from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mom's App")
        self.setFixedSize(QSize(500,400)) #can also use setMinimumSize or setMaximumSize


        button = QPushButton("שלום לכם")
        self.setCentralWidget(button)


app = QApplication([]) #manages event loop

window = MainWindow() #manages the UI - holds all other widgets
window.show()

app.exec()