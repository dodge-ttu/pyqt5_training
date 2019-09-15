import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout Widget")
        self.setGeometry(50,50,600,600)
        self.UI()

    def UI(self):
        self.gridLayout=QGridLayout()
        # btn1=QPushButton("Button 1")
        # btn2=QPushButton("Button 2")
        # btn3=QPushButton("Button 3")
        # btn4=QPushButton("Button 4")
        # self.gridLayout.addWidget(btn1,0,0)
        # self.gridLayout.addWidget(btn2,0,1)
        # self.gridLayout.addWidget(btn3,1,0)
        # self.gridLayout.addWidget(btn4,1,1)

        for i in range(0,3): # rows
            for j in range(0,4): # columns
                btn=QPushButton(f"Button {i}{j}")
                self.gridLayout.addWidget(btn,i,j)
                btn.clicked.connect(self.clickMe)

        self.setLayout(self.gridLayout)

        self.show()

    def clickMe(self):
        buttonID=self.sender().text()
        if buttonID == "Button 00":
            print("You clicked button 00")
        elif buttonID == "Button 01":
            print("You clicked button 01")
        elif buttonID == "Button 02":
            print("You clicked button 02")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__=="__main__":
    main()

