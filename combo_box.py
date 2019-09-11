import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Comboboxes")
        self.setGeometry(50,50,650,350)
        self.UI()

    def UI(self):
        self.combo=QComboBox(self)
        self.combo.move(150,100)
        button=QPushButton("Save", self)
        button.move(150,150)
        button.clicked.connect(self.getValue)
        self.combo.addItem("Python")
        self.combo.addItems(['C','C#','PHP'])
        list1=["Batman","Superman","Spiderman"]

        for name in list1:
            self.combo.addItem(name)

        for number in range(10, 101):
            self.combo.addItem(str(number))


        self.show()

    def getValue(self):
        value=self.combo.currentText()
        print(value)



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
