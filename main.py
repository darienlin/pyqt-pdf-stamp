import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QWidget

app = QApplication(sys.argv)

window = QMainWindow()
window.menuBar().addMenu("Add OpticGard Logo to Invoice")

window.show()

sys.exit(app.exec())