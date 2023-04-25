# coding=utf-8
 
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton,QPlainTextEdit,QLabel,QLineEdit,QFileDialog
import sys

line_width = len("################################################")
 
context_core = {}

class Child(QWidget):
    def __init__(self,name):
        super().__init__()
        self.win_name = name;
        self.creatUI()
    def creatUI(self):
        self.resize(1050, 650)
        self.setWindowTitle(self.win_name)
        self.openCore1 = QPushButton("Open Core:", self)
        self.openCore1.setGeometry(5,5, 100, 30)
        self.coreLabel1 = QLineEdit("Core File 1:",self)
        self.coreLabel1.setGeometry(120,5, 500, 30)
        
        self.openCore2 = QPushButton("Open Core:", self)
        self.openCore2.setGeometry(5,50, 100, 30)
        self.coreLabel2 = QLineEdit("Core File 2:",self)
        self.coreLabel2.setGeometry(120,50, 500, 30)
        
        self.compareBtn = QPushButton("Compare", self)
        self.compareBtn.setGeometry(5,90, 100, 30)
        
        self.showText1 = QPlainTextEdit("variable in core 1", self)
        self.showText1.setGeometry(10,130, 500, 500)
        self.compareText = QPlainTextEdit(self)
        self.compareText.setGeometry(510,130, 20, 500)
        self.showText2 = QPlainTextEdit("variable in core 2", self)
        self.showText2.setGeometry(530,130, 500, 500)

        self.openCore1.clicked.connect(self.openCoreLog1)
        self.openCore2.clicked.connect(self.openCoreLog2)
        self.compareBtn.clicked.connect(self.loadCompareCoreInfo)
    
    def openCoreLog1(self):
        file_name = QFileDialog.getOpenFileName(self)
        self.coreLabel1.setText(file_name[0])

    def openCoreLog2(self):
        file_name = QFileDialog.getOpenFileName(self)
        self.coreLabel2.setText(file_name[0])
        
    def loadCompareCoreInfo(self):
        compare_str = ''
        core1 = loadCoreFileInfo(self.coreLabel1.text())
        core2 = loadCoreFileInfo(self.coreLabel2.text())
        self.showText1.setPlainText(core1['various'])
        self.showText2.setPlainText(core2['various'])
        core1_comp = core1['various'].split('\n')
        core2_comp = core2['various'].split('\n')
        for i in range(len(core1_comp)):
            if core1_comp[i] != core2_comp[i] :
                key = 'x\n'
            else:
                key = ' \n'
            compare_str += key
            for i in range(0,len(core1_comp[i])//line_width):
                compare_str += '\n'
        print(compare_str)
        self.compareText.setPlainText(compare_str)
            

class CoreAnylyseTools(QWidget):
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
        self.compareVar = QPushButton("Compare Var", self)
        x_inter = 200
        icon_inter = 40
        self.showreg.setGeometry(5,x_inter, 100, 30)
        x_inter += icon_inter
        self.showbt.setGeometry(5,x_inter, 100, 30)
        x_inter += icon_inter
        self.showams.setGeometry(5,x_inter,100, 30)
        x_inter += icon_inter
        self.showvar.setGeometry(5,x_inter,100, 30)
        x_inter += icon_inter
        self.compareVar.setGeometry(5,x_inter,100, 30)
 
        self.showreg.clicked.connect(self.showregContext)
        self.showbt.clicked.connect(self.showbtContext)
        self.showams.clicked.connect(self.showasmContext)
        self.showvar.clicked.connect(self.showvarContext)
        self.compareVar.clicked.connect(self.showCompareWin)
        
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
        self.win = Child("Test Window")
        self.win.creatUI()
    def showCompareWin(self):
        self.win = Child("Compare Variable Window")
        self.win.creatUI()
        self.win.show()
        

def loadCoreFileInfo(path):
    print(path)
    context_tmp = {}
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
            context_tmp[type_context]=context
            context = ''
            type_context = None
        else:
            pass

    fd.close()
    return context_tmp
        
            
 
if __name__ == '__main__':
    core_analyse_path = r"/home/ptcs/cjh/debugTools/test/log"
    context_core = loadCoreFileInfo(core_analyse_path)
    
    app = QApplication(sys.argv)
    ex = CoreAnylyseTools()
    ex.show()
    sys.exit(app.exec_())
    