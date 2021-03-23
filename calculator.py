from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QRadioButton
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("calculator.ui", self)
        self.res=[]
        self.final=0
        self.final1=0
        self.charr=""
        # find the widgets in the xml file
        self.display=self.findChild(QTextEdit,"textEdit")   
        self.button1 = self.findChild(QPushButton, "pushButton_1")    
        self.button2 = self.findChild(QPushButton, "pushButton_2") 
        self.button3 = self.findChild(QPushButton, "pushButton_3") 
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6") 
        self.button7 = self.findChild(QPushButton, "pushButton_7") 
        self.button8 = self.findChild(QPushButton, "pushButton_8") 
        self.button9 = self.findChild(QPushButton, "pushButton_9") 
        self.button0 = self.findChild(QPushButton, "pushButton_0")   
        self.button_add = self.findChild(QPushButton, "pushButton_add") 
        self.button_sub= self.findChild(QPushButton, "pushButton_sub") 
        self.button_mul = self.findChild(QPushButton, "pushButton_mul") 
        self.button_div = self.findChild(QPushButton, "pushButton_div") 
        self.button_ln = self.findChild(QPushButton, "pushButton_ln") 
        self.res_button = self.findChild(QPushButton, "result")   


        self.button1.clicked.connect(lambda : self.clickedBtn_res("1")) 
        self.button2.clicked.connect(lambda : self.clickedBtn_res("2")) 
        self.button3.clicked.connect(lambda : self.clickedBtn_res("3")) 
        self.button4.clicked.connect(lambda : self.clickedBtn_res("4")) 
        self.button5.clicked.connect(lambda : self.clickedBtn_res("5")) 
        self.button6.clicked.connect(lambda : self.clickedBtn_res("6")) 
        self.button7.clicked.connect(lambda : self.clickedBtn_res("7")) 
        self.button8.clicked.connect(lambda : self.clickedBtn_res("8")) 
        self.button9.clicked.connect(lambda : self.clickedBtn_res("9")) 
        self.button0.clicked.connect(lambda : self.clickedBtn_res("0")) 
        self.button_add.clicked.connect(lambda : self.clickedBtn_res("+")) 
        self.button_sub.clicked.connect(lambda : self.clickedBtn_res("-")) 
        self.button_mul.clicked.connect(lambda : self.clickedBtn_res("x")) 
        self.button_div.clicked.connect(lambda : self.clickedBtn_res("/")) 
        self.button_ln.clicked.connect(lambda : self.clickedBtn_res("ln"))
        self.res_button.clicked.connect(lambda : self.clickedBtn_res("res")) 
        #self.res_button.clicked.connect(self.clickedBtn_res)
        self.tmp=""
        
        self.show()

    def clickedBtn_res(self,a):
        self.tmp+=a
        print(self.tmp)
        if a.isnumeric():
            self.res.append(a)
            pass
        else:
            if a is "+":
                self.final=1
            if a is "-":
                self.final=2
            if a is "x":
                self.final=3
            if a is "/":
                self.final=4
            if a is "ln":
                self.final=5

        if a is "res":
            if self.final==1:
                self.final1=int(self.res[0])+int(self.res[1])
            if self.final==2:
                self.final1=int(self.res[0])-int(self.res[1])
            if self.final==3:
                self.final1=int(self.res[0])*int(self.res[1])
            if self.final==4:
                self.final1=int(self.res[0])/int(self.res[1])
            if self.final==5:
                self.final1=int(self.res[0])%int(self.res[1])  

            self.display.setText(str(self.final1))
        else:
            self.display.setText(str(self.tmp))


        print(f'final = {self.final1}')
        print(self.res)

app = QApplication(sys.argv)
window = UI()
app.exec_()