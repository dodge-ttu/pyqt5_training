import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(450,150,600,800)
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ##### PROGRESS BAR #####
        self.progressBar=QProgressBar()
        ##### BUTTONS #####
        self.addButton=QToolButton()
        self.addButton.setIcon(QIcon("./icons/add.png"))
        self.addButton.setIconSize(QSize(64,64))

    def layouts(self):
        ##### LAYOUTS #####
        self.mainLayout=QVBoxLayout()
        self.topMainLayout=QVBoxLayout()
        self.topGroupBox=QGroupBox("Music Player")
        self.topGroupBox.setStyleSheet('background-color:#00E19B;')
        self.topLayout=QHBoxLayout()
        self.middleLayout=QHBoxLayout()
        self.bottomLayout=QVBoxLayout()

        ##### ADDING WIDGETS #####
        ##### TOP LAYOUT WIDGETS #####
        self.topLayout.addWidget(self.progressBar)
        ##### Middle LAYOUT WIDGETS #####
        self.middleLayout.addWidget(self.addButton)



        self.topMainLayout.addLayout(self.topLayout)
        self.topMainLayout.addLayout(self.middleLayout)
        self.topGroupBox.setLayout(self.topMainLayout)
        self.mainLayout.addWidget(self.topGroupBox)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)



def main():
    App = QApplication(sys.argv)
    player = Player()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()
