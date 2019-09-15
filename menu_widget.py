import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(50,50,600,600)
        self.UI()

    def UI(self):
        #### MAIN MENU ####
        menuBar=self.menuBar()
        file=menuBar.addMenu("File")
        edit=menuBar.addMenu("Edit")
        code=menuBar.addMenu("Code")
        helpMenu=menuBar.addMenu("Help")
        #### SUBMENU ITEMS ####
        new=QAction("New Project", self)
        new.setShortcut("Ctrl+O")
        file.addAction(new)
        open=QAction("Open", self)
        file.addAction(open)
        exit= QAction("Exit", self)
        exit.setIcon(QIcon("/home/will/pyqt5_training/icons/pencil.svg"))
        exit.triggered.connect(self.exitFunc)
        file.addAction(exit)
        #### TOOLBAR ####
        tb=self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newTb=QAction(QIcon("/home/will/pyqt5_training/icons/world.svg"), "Data", self)
        tb.addAction(newTb)
        openTb=QAction(QIcon("/home/will/pyqt5_training/icons/archive-2.svg"), "Open", self)
        tb.addAction(openTb)
        saveTb=QAction(QIcon("/home/will/pyqt5_training/icons/send-2.svg"), "Save", self)
        tb.addAction(saveTb)
        exitTb=QAction(QIcon("/home/will/pyqt5_training/icons/flash-21.svg"), "Exit", self)
        exitTb.triggered.connect(self.exitFunc)
        tb.addAction(exitTb)
        tb.actionTriggered.connect(self.btnFunc)
        self.combo=QComboBox()
        self.combo.addItems(["Spiderman", "Superman", "Batman"])
        tb.addWidget(self.combo)


        self.show()

    def exitFunc(self):
        mbox=QMessageBox.information(self,"Warning","Sure?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()

    def btnFunc(self, btn):
        if btn.text()=="Data":
            print("You clicked data button")
        elif btn.text()=="Open":
            print("You clicked open button")
        else:
            print("You clicked save button")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()
