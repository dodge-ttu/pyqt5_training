import sys
from PyQt5.QtWidgets import *


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(450,150,600,800)
        self.UI()
        self.show()

    def UI(self):
        pass


def main():
    App = QApplication(sys.argv)
    player = Player()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()
