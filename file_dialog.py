import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialog")
        self.setGeometry(50,50,600,600)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        self.editor=QTextEdit()
        fileButton=QPushButton("Open File")
        fileButton.clicked.connect(self.openFile)
        fontButton=QPushButton("Change Font")
        fontButton.clicked.connect(self.changeFont)
        colorButton=QPushButton("Chane Color")
        colorButton.clicked.connect(self.changeColor)
        hbox.addStretch()
        hbox.addWidget(fontButton)
        hbox.addWidget(colorButton)
        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addWidget(fileButton)
        hbox.addStretch()

        self.setLayout(vbox)

        self.show()

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)

    def changeColor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)

    def openFile(self):
        url=QFileDialog.getOpenFileName(self, "Open a file", "All Files(*);;*txt")
        print(url)
        fileUrl=url[0]
        print(fileUrl)
        with open(fileUrl, 'r') as file:
            content = file.read()
        self.editor.setText(content)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__=="__main__":
    main()

