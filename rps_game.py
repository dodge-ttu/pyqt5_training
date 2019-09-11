import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)
computerScore = 0
playerScore = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors Game")
        self.setGeometry(350,350,650,400)
        self.UI()

    def UI(self):
        #### SCORES ####
        self.scoreComputerText=QLabel("Computer Score:   ", self)
        self.scoreComputerText.move(30,20)
        self.scoreComputerText.setFont(textFont)
        self.scorePlayerText=QLabel("Player Score:   ", self)
        self.scorePlayerText.move(400,20)
        self.scorePlayerText.setFont(textFont)
        #### Images ####
        self.imageComputer=QLabel(self)
        self.imageComputer.setPixmap(QPixmap("/home/will/pyqt5_training/images/rock.png"))
        self.imageComputer.move(50,100)
        self.imagePlayer=QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("/home/will/pyqt5_training/images/rock.png"))
        self.imagePlayer.move(450,100)
        self.imageGame=QLabel(self)
        self.imageGame.setPixmap(QPixmap("/home/will/pyqt5_training/images/game.png"))
        self.imageGame.move(300,160)
        #### BUTTONS ####
        self.btnStart=QPushButton("Start", self)
        self.btnStart.setFont(buttonFont)
        self.btnStart.clicked.connect(self.start)
        self.btnStart.move(75,250)
        self.btnStop=QPushButton("Stop", self)
        self.btnStop.clicked.connect(self.stop)
        self.btnStop.setFont(buttonFont)
        self.btnStop.move(475,250)
        #### TIMER ####
        self.timer=QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def playGame(self):
        self.randComputer=randint(1,3)
        if self.randComputer == 1:
            self.imageComputer.setPixmap(QPixmap("/home/will/pyqt5_training/images/rock.png"))
        elif self.randComputer == 2:
            self.imageComputer.setPixmap(QPixmap("/home/will/pyqt5_training/images/paper.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("/home/will/pyqt5_training/images/scissors.png"))

        self.randPlayer=randint(1,3)
        if self.randPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("/home/will/pyqt5_training/images/rock.png"))
        elif self.randPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("/home/will/pyqt5_training/images/paper.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("/home/will/pyqt5_training/images/scissors.png"))

    def start(self):
        self.timer.start()

    def stop(self):
        global computerScore
        global playerScore

        self.timer.stop()

        if self.randComputer == self.randPlayer:
            mbox=QMessageBox.information(self, "Game Info", "Draw Game")

        elif self.randComputer == 1 and self.randPlayer == 2:
            mbox=QMessageBox.information(self, "Game Info", "You Win")
            playerScore+=1
            self.scorePlayerText.setText(f"Player Score: {playerScore}")

        elif self.randComputer == 1 and self.randPlayer == 3:
            mbox=QMessageBox.information(self, "Game Info", "Computer Wins")
            computerScore+=1
            self.scoreComputerText.setText(f"Computer Score: {computerScore}")

        elif self.randComputer == 2 and self.randPlayer == 1:
            mbox=QMessageBox.information(self, "Game Info", "Computer Wins")
            computerScore+=1
            self.scoreComputerText.setText(f"Computer Score: {computerScore}")

        elif self.randComputer == 2 and self.randPlayer == 3:
            mbox=QMessageBox.information(self, "Game Info", "You Win")
            playerScore+=1
            self.scorePlayerText.setText(f"Player Score: {playerScore}")

        elif self.randComputer == 3 and self.randPlayer == 1:
            mbox=QMessageBox.information(self, "Game Info", "You Win")
            playerScore+=1
            self.scorePlayerText.setText(f"Player Score: {playerScore}")

        elif self.randComputer == 3 and self.randPlayer == 2:
            mbox=QMessageBox.information(self, "Game Info", "Computer Wins")
            computerScore+=1
            self.scoreComputerText.setText(f"Computer Score: {computerScore}")

        if computerScore == 3 or playerScore ==3:
            mbox=QMessageBox.information(self, "Game Info", "Game Over")
            sys.exit()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()
