import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Timer")
        self.setGeometry(250,150,400,400)
        self.UI()

    def UI(self):
        self.colorLabel=QLabel(self)
        self.colorLabel.resize(250,250)
        self.colorLabel.setStyleSheet("background-color:green")
        self.colorLabel.move(80,20)
        #### BUTTONS ####
        btnStart=QPushButton("Start",self)
        btnStop=QPushButton("Stop",self)
        btnStart.move(80,300)
        btnStop.move(190,300)
        btnStart.clicked.connect(self.start)
        btnStop.clicked.connect(self.stop)
        #### TIMER ####
        self.timer=QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.changeColor)
        self.value=0

        self.show()

    def changeColor(self):
        if self.value==0:
            self.colorLabel.setStyleSheet("background-color:yellow")
            self.value=1
        else:
            self.colorLabel.setStyleSheet("background-color:red")
            self.value=0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

def main():
    App = QApplication(sys.argv)
    window = Window()
    window.start()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
