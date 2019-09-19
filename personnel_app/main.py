import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
import sqlite3
from PIL import Image
import os


con = sqlite3.connect("employees.db")
cur = con.cursor()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        self.employeeList=QListWidget()
        self.btnNew=QPushButton("New")
        self.btnNew.setStyleSheet("background-color:#C6FFB0")
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate=QPushButton("Update")
        self.btnUpdate.setStyleSheet("background-color:#C6FFB0")
        self.btnDelete=QPushButton("Delete")
        self.btnDelete.setStyleSheet("background-color:#C6FFB0")

    def layouts(self):
        # Main Layout.
        self.setStyleSheet("background-color:#E7FDFF")
        self.mainLayout=QHBoxLayout()
        self.leftLayout=QFormLayout()
        self.rightMainLayout=QVBoxLayout()
        self.rightTopLayout=QHBoxLayout()
        self.rightBottomLayout=QHBoxLayout()
        # Add child layouts to main layout.
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 40)  # 40 % of window space.
        self.mainLayout.addLayout(self.rightMainLayout, 60)  # 60 % of window space.
        # Add widgets to layouts.
        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        # Set main window layout.
        self.setLayout(self.mainLayout)

    def addEmployee(self):
        self.newEmoloyee=AddEmployee()
        self.close()


class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.defaultImage = "/home/will/pyqt5_training/personnel_app/images/bowfly.jpg"
        self.setWindowTitle("Add Employees")
        self.setGeometry(450,150,600,800)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        # Top layout widgets.
        self.title=QLabel("Add Person")
        self.title.setStyleSheet("font-size: 24pt; font-family:Arial Bold;")
        self.imgAdd=QLabel()
        self.imgAdd.setPixmap(QPixmap("/home/will/pyqt5_training/personnel_app/icons/spaceship.svg"))
        # Bottom layout widgets.
        self.nameLbl=QLabel("Name: ")
        self.nameEntry=QLineEdit()
        self.nameEntry.setPlaceholderText("Enter employee name")
        self.surnameLbl=QLabel("Surname: ")
        self.surnameEntry=QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter employee surname")
        self.phoneLbl=QLabel("Phone: ")
        self.phoneEntry=QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter employee phone")
        self.emailLbl=QLabel("Email: ")
        self.emailEntry=QLineEdit()
        self.emailEntry.setPlaceholderText("Enter employee email")
        self.imgLbl=QLabel("Picture: ")
        self.imgButton=QPushButton("Browse")
        self.imgButton.setStyleSheet("background-color:#C6FFB0")
        self.imgButton.clicked.connect(self.uploadImage)
        self.addressLbl=QLabel("Address: ")
        self.addressEditor=QTextEdit()
        self.addButton=QPushButton("Add")
        self.addButton.setStyleSheet("background-color:#C6FFB0")
        self.addButton.clicked.connect(self.addEmployee)

    def layouts(self):
        # Creating main layout.
        self.setStyleSheet("background-color:#E7FDFF")
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        # Adding child layouts to main layout.
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        # Adding widgets to layout.
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110,20,10,30)  # left,top,right,bottom

        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl, self.emailEntry)
        self.bottomLayout.addRow(self.imgLbl, self.imgButton)
        self.bottomLayout.addRow(self.addressLbl, self.addressEditor)
        self.bottomLayout.addRow(self.addButton)

        # Setting main layout for window.
        self.setLayout(self.mainLayout)

    def uploadImage(self):
        size=(128,128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")

        if ok:
            newName=os.path.basename(self.fileName)
            img=Image.open(self.fileName)
            img=img.resize(size)
            img.save(os.path.join("/home/will/pyqt5_training/personnel_app/images", newName))

    def addEmployee(self):
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email=self.emailEntry.text()
        img=self.defaultImage
        address=self.addressEditor.toPlainText()

        if (name and surname and phone):
            try:
                query="INSERT INTO employees (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query,(name,surname,phone,email,img,address))
                con.commit()
                QMessageBox.information(self,"Success", "Person has been added")
            except:
                QMessageBox.information(self, "Warning", "Person has not been added.")

        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")

def main():
    App=QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()

