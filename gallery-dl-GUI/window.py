from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QFileDialog, QPushButton, QVBoxLayout, QWidget, QGridLayout
import downloader
import subprocess
import configWindow
class GUI():

    configWindow = configWindow 

    def __init__(self, configWindow = configWindow) -> None:
        self.app = QApplication([])
        self.configWindow = configWindow
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

        self.settingsbutton = QPushButton()
        self.settingsbutton.setText("Settings")
        self.settingsbutton.clicked.connect(self.spawnConfigWindow)
        
        self.downloadbutton = QPushButton()
        self.downloadbutton.setText("Download")
        self.downloadbutton.clicked.connect(self.download)

        self.box3.addWidget(self.downloadbutton, 0,0)
        self.box3.addWidget(self.settingsbutton, 0,1)

        self.parent.addLayout(self.box1,0,0)
        self.parent.addLayout(self.box2,1,0)
        self.parent.addLayout(self.box3,2,0)
        self.window.setLayout(self.parent)
        self.window.show()
        self.app.exec()

    def openfile(self):        
        file = str(QFileDialog.getExistingDirectory(None,"Select Directory")) 

        self.fileinput.setText(file)

    def spawnConfigWindow(self):
        self.configWindow.run()

    def download(self):
        url = self.urlinput.text()
        path = self.fileinput.text()
        output = subprocess.run()
        