import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Radio Buttons")
        self.setGeometry(50,50,650,350)
        self.UI()

    def UI(self):
        self.name=QLineEdit(self)
        self.name.move(150,50)
        self.name.setPlaceholderText('Enter your name')
        self.surname=QLineEdit(self)
        self.surname.move(150,100)
        self.surname.setPlaceholderText("Enter your surname")
        self.male=QRadioButton("Male", self)
        self.female=QRadioButton("Female", self)
        self.male.move(150,150)
        self.male.setChecked(True)
        self.female.move(260,150)
        button=QPushButton("Submit",self)
        button.clicked.connect(self.getValues)
        button.move(220,200)

        self.show()

    def getValues(self):
        name=self.name.text()
        surname=self.surname.text()
        if self.male.isChecked():
            print(name+" "+surname+" you are a male")
        else:
            print(name+" "+surname+" you are a female")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
