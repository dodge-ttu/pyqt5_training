import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50,50,700,1000)
        self.UI()

    def UI(self):
        self.image=QLabel(self)
        self.image.setPixmap(QPixmap('/home/will/pyqt5_training/images/fun_img.png'))
        self.image.move(100,10)
        removeButton=QPushButton('Remove', self)
        removeButton.move(200,800)
        removeButton.clicked.connect(self.removeImg)
        showButton=QPushButton('Show', self)
        showButton.move(400,800)
        showButton.clicked.connect(self.showImg)
        self.show()

    def showImg(self):
        self.image.show()

    def removeImg(self):
        self.image.close()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
