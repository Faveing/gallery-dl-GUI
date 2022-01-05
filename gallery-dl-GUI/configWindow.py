from PyQt5.QtWidgets import QApplication, QRadioButton, QPushButton, QLineEdit, QLabel, QFileDialog, QWidget
import typing 

class configWindow(QApplication):
    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)
        self.root = QWidget()

    def run(self):
        self.root.show() 