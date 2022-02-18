from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("design.ui", self)
        self.button = self.findChild(QPushButton, "btn")
        self.label = self.findChild(QLabel, "label")
        self.button.clicked.connect(self.clicker)
        self.show()

    def clicker(self):
        file_name = QFileDialog.getOpenFileName(
            self, "Open Image", "/root/", "JPG(*.jpg)")
        if file_name:
            self.pixmap = QPixmap(file_name[0])
            self.label.setPixmap(self.pixmap)


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
