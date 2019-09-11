import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using list widget")
        self.setGeometry(50,50,650,350)
        self.UI()

    def UI(self):
        self.addRecord=QLineEdit(self)
        self.addRecord.move(100,50)
        self.listWidget=QListWidget(self)
        self.listWidget.move(100,100)
        #### BUTTONS ####
        btnAdd=QPushButton("Add",self)
        btnAdd.move(400, 50)
        btnAdd.clicked.connect(self.funcAdd)
        btnDelete=QPushButton("Delete",self)
        btnDelete.clicked.connect(self.funcDelete)
        btnDelete.move(400,100)
        btnGet=QPushButton("Get",self)
        btnGet.move(400,150)
        btnGet.clicked.connect(self.funcGet)
        btnDeleteAll=QPushButton("Delete All",self)
        btnDeleteAll.move(400,200)
        btnDeleteAll.clicked.connect(self.funcDeleteAll)

        self.show()

    def funcAdd(self):
        val=self.addRecord.text()
        self.listWidget.addItem(val)
        self.addRecord.setText("")

    def funcDelete(self):
        id=self.listWidget.currentRow()
        print(id)
        self.listWidget.takeItem(id)

    def funcGet(self):
        val=self.listWidget.currentItem().text()
        print(val)

    def funcDeleteAll(self):
        self.listWidget.clear()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
