# coding=utf-8
 
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton,QPlainTextEdit
import sys
 
context_core = {}

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.resize(1200, 700)
        self.setWindowTitle('codedump analyze tool')
        self.CreatUI()
 
    def CreatUI(self):
        self.showreg = QPushButton("Show register", self)
        self.showbt = QPushButton("Show backtrace", self)
        self.showams = QPushButton("Show ASM", self)
        self.showvar = QPushButton("Show Variable", self)
        x_inter = 200
        self.showreg.setGeometry(5,x_inter, 100, 30)
        x_inter += 35
        self.showbt.setGeometry(5,x_inter, 100, 30)
        x_inter += 35
        self.showams.setGeometry(5,x_inter,100, 30)
        x_inter += 35
        self.showvar.setGeometry(5,x_inter,100, 30)
 
        self.showreg.clicked.connect(self.showregContext)
        self.showbt.clicked.connect(self.showbtContext)
        self.showams.clicked.connect(self.showasmContext)
        self.showvar.clicked.connect(self.showvarContext)
        
        self.showinfo = QPlainTextEdit(" core Information", self)
        self.showinfo.setGeometry(150,10, 1000, 650)
 
    def addWidget(self):
        self.CreatUI()
        self.showWidget()
 
    def showWidget(self):
        self.showreg.show()
        self.showbt.show()
        self.showams.show()
        self.showvar.show()
    
    def showregContext(self):
        self.showinfo.setPlainText(context_core['register'])
    def showbtContext(self):
        self.showinfo.setPlainText(context_core['bt'])
    def showasmContext(self):
        self.showinfo.setPlainText(context_core['asm'])
    def showvarContext(self):
        self.showinfo.setPlainText(context_core['various'])
    def showTestContext(self):
        self.showinfo.setPlainText("aaa\n bbb\n")
        

def loadCoreFileInfo(path):
    global context_core
    type_context = None
    start = False
    context = ''
    #with open(path,'r') as fd:
    line = True
    fd = open(path,'r')
    while line:
        line = fd.readline()
        if start :
            if not "<==end" in line:
                context += line
            
        if "@#$info-registers:" in line:
            type_context = 'register'
            start = True
        elif "@#$info-bt:" in line:
            type_context = 'bt'
            start = True
        elif "@#$info-asm:" in line:
            type_context = 'asm'
            start = True
        elif "@#$info-global_various:" in line:
            type_context = 'various'
            start = True
        elif "<==end" in line:
            start = False
            context_core[type_context]=context
            context = ''
            type_context = None
        else:
            pass

    fd.close()
        
            
 
if __name__ == '__main__':
    core_analyse_path = r"test/log"
    loadCoreFileInfo(core_analyse_path)
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
    
