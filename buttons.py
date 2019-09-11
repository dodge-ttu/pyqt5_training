from PyQt5.QtWidgets import *

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50,50,650,350)
        self.UI()

    def UI(self):
        self.text=QLabel("My Text", self)
        self.text.move(33,33)
        enterButton=QPushButton("Enter", self)
        exitButton=QPushButton("Exit", self)
        enterButton.move(100,80)
        exitButton.move(200,80)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.text.setText("You clicked Enter")
        self.text.resize(350,30)
    def exitFunc(self):
        self.text.setText("You clicked Exit")
        self.text.resize(350,30)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
