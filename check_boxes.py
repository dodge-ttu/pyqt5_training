import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50,50,650,350)
        self.UI()

    def UI(self):
        self.name=QLineEdit(self)
        self.surname=QLineEdit(self)
        self.name.setPlaceholderText('Enter your name')
        self.surname.setPlaceholderText('Enter your name')
        self.name.move(150,50)
        self.surname.move(150,100)
        self.remember=QCheckBox('Remember me', self)
        self.remember.move(180,150)
        button=QPushButton('Submit', self)
        button.move(200,200)
        button.clicked.connect(self.submit)

        self.show()

    def submit(self):
        if self.remember.isChecked():
            print(f'Name: {self.name.text()} Surname: {self.surname.text()} Remember checked')
        else:
            print(f'Name: {self.name.text()} Surname: {self.surname.text()} Remember not checked')


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
