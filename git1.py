import os
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *

class calculate(QMainWindow):
    st=list()
    example=['*',"-","+","/"]
    y=""
    k=""
    def __init__(self):
        super().__init__()
        #main window
        self.setMinimumSize(380,740)
        self.setMaximumSize(380,740)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon(os.getcwd() + "\\resource\\redmi.ico"))
        self.setStyleSheet("background-color: rgb(10,10,10)")
    #line1
        self.linmain=QLineEdit("",self)
        self.linmain.setGeometry(20,240,340,60)
        self.linmain.setStyleSheet("""background-color : rgb(10,10,10);
                                            color :rgb(128,128,128);
                                            border-color: black;
                                            border-style: solid;                    
                                                                """)
        self.linmain.setFont(QFont("Arial",16))
        self.linmain.setAlignment(Qt.AlignRight)
    #line2
        self.lin1=QLineEdit("",self)
        self.lin1.setGeometry(20,180,340,60)
        self.lin1.setStyleSheet("""background-color : rgb(10,10,10);
                                    color :rgb(240,240,240);
                                    border-color: black;
                                    border-style: solid;                    
                                                        """)
        self.lin1.setFont(QFont("Arial",35))
        self.lin1.setAlignment(Qt.AlignRight)
    # line3
        self.lin3 = QLineEdit("", self)
        self.lin3.setGeometry(15, 375, 350, 1)
        self.lin3.setStyleSheet("""background-color :rgb(10,10,10);
                                            color :rgb(128,128,128);
                                            border-color:rgb(128,128,128)  ;
                                            border-style: solid;
                                            border-width: 3px                    
                                                                """)
        self.lin3.setFont(QFont("Regular", 1))
    # button AC
        self.bnac = self.charakter("ac.png")
        self.bnac.setGeometry(20,392,60,30)

    # button 🡠
        bnback = self.charakter("back.png")
        bnback.setGeometry(113,392, 60,30)
        bnback.clicked.connect(lambda : self.son_add("<"))
    # button %
        bnf = self.charakter("percent.png")
        bnf.setGeometry(206,392, 60, 30)
    # button ÷
        bnb = self.charakter("boluv.png")
        bnb.setGeometry(300,392, 60, 25)
        bnb.clicked.connect(lambda: self.son_add("/"))
    # button 7
        bn7 = self.number("7")
        bn7.setGeometry(20, 466, 60, 30)
        bn7.clicked.connect(lambda :self.son_add("7"))
    # button 8
        bn8 = self.number("8")
        bn8.setGeometry(113,466,60,30)
        bn8.clicked.connect(lambda : self.son_add("8"))
    #button 9
        bn9= self.number("9")
        bn9.setGeometry(206,466,60,30)
        bn9.clicked.connect(lambda: self.son_add("9"))
    #button ×
        bnx=self.charakter("kopaytiruv.png")
        bnx.setGeometry(300,466,60,30)
        bnx.clicked.connect(lambda: self.son_add("*"))
    #button 5
        bn5=self.number("5")
        bn5.setGeometry(113,540,60,30)
        bn5.clicked.connect(lambda: self.son_add("5"))
    #button 6
        bn6=self.number("6")
        bn6.setGeometry(206,540,60,30)
        bn6.clicked.connect(lambda: self.son_add("6"))
    #button -

        bnmin = self.charakter("minus.png")
        bnmin.setGeometry(300, 540, 60, 30)
        bnmin.clicked.connect(lambda: self.son_add("-"))
    #button 2
        bn2=self.number("2")
        bn2.setGeometry(113,614,60,30)
        bn2.clicked.connect(lambda: self.son_add("2"))
    #button 3
        bn3=self.number("3")
        bn3.setGeometry(206,614,60,30)
        bn3.clicked.connect(lambda: self.son_add("3"))
    #button 0
        bn0=self.number("0")
        bn0.setGeometry(113,690,60,30)
        bn0.clicked.connect(lambda: self.son_add("0"))
    #button ,
        bnver=self.number("′")
        bnver.setGeometry(206,690,60,30)
        bnver.clicked.connect(lambda : self.son_add("."))
    #button=
        bnteng = QPushButton("=", self)
        bnteng.setStyleSheet("""background-color: rgb(255,69,0);color : rgb(240,240,240);
                             border-radius: 25px;
                             border-style: solid;
                             """)
        bnteng.setFont(QFont("Regular",20))
        bnteng.setGeometry(305,680,50,50)
        bnteng.clicked.connect(self.hisobla)
    #button +
        bnplu=self.charakter("plus.png")
        bnplu.setGeometry(300,614,60,30)
        bnplu.clicked.connect(lambda: self.son_add("+"))
    # button 4
        bn4 = self.number("4")
        bn4.setGeometry(20, 540, 60, 30)
        bn4.clicked.connect(lambda: self.son_add("4"))
    # button 1
        bn1 = self.number("1")
        bn1.setGeometry(20,614,60, 30)
        bn1.clicked.connect(lambda: self.son_add("1"))
    # button ↻
        bnk = QPushButton(self)
        bnk.setIcon(QIcon(QPixmap(os.getcwd() + "\\resource\\almash.png")))
        bnk.setGeometry(20, 690, 60, 30)
        bnk.setStyleSheet("background-color:  rgb(10,10,10);")
    def number(self,n):
        bn = QPushButton(n, self)
        bn.setStyleSheet("background-color: rgb(10,10,10);color : rgb(240,240,240)")
        bn.setFont(QFont("Microsoft Sans Serif", 20))
        return bn
    def charakter(self,k):
        bn = QPushButton(self)
        bn.setIcon(QIcon(QPixmap(os.getcwd() + "\\resource\\"+k)))
        bn.setStyleSheet("background-color:  rgb(10,10,10);")
        return bn
    def hisobla(self):
        try:
            calculate.st.append(self.lin1.text())
            self.lin1.setStyleSheet("""background-color : rgb(10,10,10);
                                                color :rgb(240,240,240);
                                                border-color: black;
                                                border-style: solid;                    
                                                                    """)
            self.lin1.setFont(QFont("Arial", 15))
            self.lin1.setText(self.lin1.text())
            ans=eval("".join(calculate.st))

            self.linmain.setStyleSheet("""background-color : rgb(10,10,10);
                                                    color :rgb(240,240,240);
                                                    border-color: black;
                                                    border-style: solid;                    
                                                                        """)
            self.linmain.setFont(QFont("Arial", 35))
            self.linmain.setText("=" + str(ans))
            calculate.st.clear()
        except:
            pass
    def son_add(self,x):
        match x:
            case x.isdigit():
                self.lin1.setText(self.lin1.text()+x)
                self.lin1.setText('=' + str(eval(self.linmain.text())))
            case "<":
                calculate.y += (self.lin1.text())
                calculate.y = calculate.y[:-1]
                self.lin1.setText(calculate.y)
                calculate.y=""
            case calculate.k :
                if x in calculate.example:
                    calculate.y=self.lin1.text()
                    calculate.y=calculate.y[:-1]
                    self.lin1.setText(calculate.y)
                    calculate.y=""
        calculate.k=x

app = QApplication(sys.argv)
cal = calculate()
cal.show()
sys.exit(app.exec_())