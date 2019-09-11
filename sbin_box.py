import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times",16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50,50,650,350)
        self.UI()

    def UI(self):
        self.spinBox=QSpinBox(self)
        self.spinBox.move(150,100)
        self.spinBox.setFont(font)
        self.spinBox.setRange(25,110)
        self.spinBox.setSingleStep(5)
        self.spinBox.valueChanged.connect(self.getValue)
        button=QPushButton("Send", self)
        button.move(150,170)
        button.clicked.connect(self.getValue)

        self.show()

    def getValue(self):
        value=self.spinBox.value()
        print(value)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
