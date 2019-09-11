import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times",12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Message Boxes")
        self.setGeometry(50,50,650,350)
        self.UI()

    def UI(self):
        button=QPushButton("Click Me!",self)
        button.setFont(font)
        button.move(200,150)
        button.clicked.connect(self.messageBox)

        self.show()

    def messageBox(self):
        # mbox=QMessageBox.question(self, "Warning!!!", "Are you sure?" \
        #                          ,QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        # if mbox==QMessageBox.Yes:
        #    sys.exit()
        # elif mbox==QMessageBox.No:
        #    print("You clicked no button")
        mbox=QMessageBox.information(self,"Information", "You logged out")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
