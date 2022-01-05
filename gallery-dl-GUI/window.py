from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QFileDialog, QPushButton, QVBoxLayout, QWidget, QGridLayout

class GUI():

    def __init__(self) -> None:
        self.app = QApplication([])
        self.window = QWidget()
        self.parent = QGridLayout()
        self.box1 = QGridLayout()
        self.box2 = QGridLayout()
        self.box3 = QGridLayout()

        self.urlinput = QLineEdit()
        
        self.box1.addWidget(QLabel(text="URL:"),0,0)
        self.box1.addWidget(self.urlinput,0,1)

        self.filebutton = QPushButton()
        self.filebutton.setText("Browse")
        self.filebutton.clicked.connect(self.openfile)

        self.fileinput = QLineEdit()

        self.box2.addWidget(QLabel(text="Path:"),0,0)
        self.box2.addWidget(self.fileinput, 0,1)
        self.box2.addWidget(self.filebutton,0,2)

        self.downloadbutton = QPushButton()
        self.downloadbutton.setText("Download")
        self.downloadbutton.clicked.connect(self.download)

        self.box3.addWidget(self.downloadbutton, 0,0)

        self.parent.addLayout(self.box1,0,0)
        self.parent.addLayout(self.box2,1,0)
        self.parent.addLayout(self.box3,2,0)
        self.window.setLayout(self.parent)
        self.window.show()
        self.app.exec()

    def openfile(self):        
        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()","", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")

        self.fileinput.setText(file)


    def download(self):
        print("test")