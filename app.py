import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class OpticGardInvoiceHeader(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpticGard Invoice Header")
        layout = QVBoxLayout()
        self.label = QLabel('OpticGard Header Scripts')
        layout.addWidget(self.label)
        self.setLayout(layout)
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpticGard Scripts")

        #creates the button and the action
        button_action = QAction('Open Opticgard Invoice Header', self)
        button_action.triggered.connect(self.show_opticgard_invoice_header)
        button_action.setCheckable(True)

        # Create the menu bar and add it to the main window
        menubar = self.menuBar()
        widget_menu = menubar.addMenu(" &Widget")
        widget_menu.addAction(button_action)

        label = QLabel('OpticGard Scripts\nPlease click widgets to start.')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

    def show_opticgard_invoice_header(self, checked):
        self.window = OpticGardInvoiceHeader()
        self.window.show()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
