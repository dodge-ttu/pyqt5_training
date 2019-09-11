import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Line Edits")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
        self.nameTextBox=QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please Enter your name")
        self.nameTextBox.move(60,80)
        self.passTextBox=QLineEdit(self)
        self.passTextBox.move(60,150)
        self.passTextBox.setPlaceholderText("Please Enter your password")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        button = QPushButton("Save", self)
        button.move(220,220)
        button.clicked.connect(self.getValues)
        self.show()

    def getValues(self):
        name=self.nameTextBox.text()
        password=self.passTextBox.text()
        self.setWindowTitle(f"Name:{name} Password:{password}")
        print(name, password)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
