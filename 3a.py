from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QRadioButton
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("importui.ui", self)

        # find the widgets in the xml file
        self.numA=self.findChild(QTextEdit,"textEdit")
        self.numB=self.findChild(QTextEdit,"textEdit_2")
        self.plusradio = self.findChild(QRadioButton, "cong")
        self.minusradio = self.findChild(QRadioButton, "tru")
        self.result = self.findChild(QTextEdit, "ketqua")     
        self.button = self.findChild(QPushButton, "chon")        
        self.button.clicked.connect(self.clickedBtn)
        self.sum=0
        self.show()

    def clickedBtn(self):
        number1=int(self.textEdit.toPlainText())
        number2=int(self.textEdit_2.toPlainText())
        if self.plusradio.isChecked()== True:
            kq="cong"
            self.sum=number1+number2
        if self.minusradio.isChecked()== True:
            kq="tru"
            self.sum=number1-number2
        self.sum=str(self.sum)
        self.result.setText(self.sum)

app = QApplication(sys.argv)
window = UI()
app.exec_()