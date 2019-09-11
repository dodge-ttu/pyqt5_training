import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50,50,650,350)
        self.UI()

    def UI(self):
        text=QLabel("Hello Python", self)
        text2=QLabel("Hello World", self)
        text.move(100,50)
        text2.move(400,50)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
