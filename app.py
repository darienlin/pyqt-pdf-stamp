import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class OpticGardInvoiceHeader(QWidget):
    def __init__(self):
        super().__init__()

        #variables
        self.fileName = ''

        #title
        self.setWindowTitle("OpticGard Invoice Header")
        layout1 = QVBoxLayout()
        label = QLabel('OpticGard Header Scripts')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFixedHeight(25)
        layout1.addWidget(label)

        #drag and drop
        layout2 = QHBoxLayout()
        label2 = QLabel('Drag and drop pdf file here')
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout2.addWidget(label2)

        #layout for right side
        layout6 = QVBoxLayout()

        #choose file
        layout3 = QVBoxLayout()
        self.fileLabel = QLabel('No File Selected')
        self.fileLabel.setFixedHeight(15)
        chooseFileButton = QPushButton('Choose File')
        chooseFileButton.clicked.connect(self.open_pdf)
        layout3.addWidget(self.fileLabel)
        layout3.addWidget(chooseFileButton)
        layout6.addLayout(layout3)

        #output directory
        layout4 = QVBoxLayout()
        self.outputDir = QLabel('No Output Selected')
        self.outputDir.setFixedHeight(15)
        self.outputDir.setWordWrap(True)
        chooseOutputDir = QPushButton('Choose Output Location')
        chooseOutputDir.clicked.connect(self.output_dir)
        layout4.addWidget(self.outputDir)
        layout4.addWidget(chooseOutputDir)
        layout6.addLayout(layout4)



        #invoice/sales selection
        layout5 = QVBoxLayout()
        label3 = QLabel('Invoice/Sales Order')
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout6.addWidget(label3)



        layout1.addLayout(layout2)
        layout2.addLayout(layout6)

        self.setLayout(layout1)

    #function to opens the pdf user wants to stamp
    def open_pdf(self):
        fileName = QFileDialog.getOpenFileName(self,
            "Open PDF", "/Desktop", "PDF Files (*.pdf)")

        if fileName:
            self.fileLabel.setText(f"Selected file: {os.path.basename(fileName[0])}")

    #function to select the output directory
    def output_dir(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')

        if folderpath:
            self.outputDir.setText(f"Selected Location: {folderpath}")

        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpticGard Scripts")

        #creates window references
        self.invoiceWindow = None

        #creates the button and the action
        button_action = QAction('Open Opticgard Invoice Header', self)
        button_action.triggered.connect(self.show_opticgard_invoice_header)
        button_action.setCheckable(True)

        # Create the menu bar and add it to the main window
        menubar = self.menuBar()
        widget_menu = menubar.addMenu(" &Widget")
        widget_menu.addAction(button_action)

        #main text that shows up when you run the widget
        label = QLabel('OpticGard Scripts\nPlease click widgets to start.')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

    #function that opens and closes the new window
    def show_opticgard_invoice_header(self, checked):
        if self.invoiceWindow == None:
            self.invoiceWindow = OpticGardInvoiceHeader()
            self.invoiceWindow.resize(700, 500)
            self.invoiceWindow.show()
        else:
            self.invoiceWindow.close()
            self.invoiceWindow = None



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
