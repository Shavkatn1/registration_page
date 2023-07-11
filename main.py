import sys
import csv
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
class RegistrationPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:grey;")
        name_label=QtWidgets.QLabel("Ism:")
        name_label.setStyleSheet("color:green;font:bold;font-size:12pt")
        self.name_edit=QtWidgets.QLineEdit()
        self.name_edit.setStyleSheet("""border:2px solid green;
                                        background-color:white;
                                        border-radius: 50%;""")
        surname_label=QtWidgets.QLabel('Familiya:')
        surname_label.setStyleSheet("color:green;font:bold;font-size:12pt")
        self.surname_edit=QtWidgets.QLineEdit()
        self.surname_edit.setStyleSheet("""border:2px solid green;
                                        background-color:white;
                                        border-radius: 50%;""")
        jins_label=QtWidgets.QLabel('Jinsi:')
        jins_label.setStyleSheet("color:green;font:bold;font-size:12pt")
        female_radio=QtWidgets.QRadioButton("Ayol")
        female_radio.setStyleSheet("""border:2px solid green;
                                        background-color:pink;
                                        border-radius: 50%;""")
        female_radio.setFixedWidth(50)
        male_radio=QtWidgets.QRadioButton("Erkak")
        male_radio.setStyleSheet("""border:2px solid green;
                                        background-color:pink;
                                        border-radius: 50%;""")
        male_radio.setFixedWidth(55)
        login_label=QtWidgets.QLabel('Login:')
        login_label.setStyleSheet("color:green;font:bold;font-size:12pt")
        self.login_edit=QtWidgets.QLineEdit()
        self.login_edit.setStyleSheet("""border:2px solid green;
                                        background-color:white;
                                        border-radius: 50%;""")
        parol_label=QtWidgets.QLabel('Parol:')
        parol_label.setStyleSheet("color:green;font:bold;font-size:12pt")
        self.parol_edit=QtWidgets.QLineEdit()
        self.parol_edit.echoMode()
        self.parol_edit.setStyleSheet("""border:2px solid green;
                                        background-color:white;
                                        border-radius: 50%;""")
        parol2_label=QtWidgets.QLabel('Parol_2:')
        parol2_label.setStyleSheet("color:green;font:bold;font-size:12pt")
        self.parol2_edit=QtWidgets.QLineEdit()
        self.parol2_edit.setStyleSheet("""border:2px solid green;
                                        background-color:white;
                                        border-radius: 50%;""")
        register_button=QtWidgets.QPushButton("Register")
        register_button.setStyleSheet("""border:2px solid green;
                                                background-color:black;
                                                border-radius: 50%;
                                                color:green;font-size:16pt""")
        check_label = QtWidgets.QCheckBox("""Malumotni faylga 
saqlashga roziman""")
        check_label.setStyleSheet("color:green;font:bold;font-size:8pt;")
        register_button.clicked.connect(self.submit)



        grid=QtWidgets.QGridLayout()
        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_edit,0,1)
        grid.addWidget(surname_label,1,0)
        grid.addWidget(self.surname_edit,1,1)
        grid.addWidget(jins_label,2,0)
        grid.addWidget(female_radio,2,1)
        grid.addWidget(male_radio,2,2)
        grid.addWidget(login_label,3,0)
        grid.addWidget(self.login_edit,3,1)
        grid.addWidget(parol_label,4,0)
        grid.addWidget(self.parol_edit,4,1)
        grid.addWidget(parol2_label,5,0)
        grid.addWidget(self.parol2_edit,5,1)
        grid.addWidget(check_label,6,0)
        grid.addWidget(register_button,7,1)
        self.setLayout(grid)
    def submit(self):
        name = self.name_edit.text().strip()
        surname = self.surname_edit.text().strip()
        login = self.login_edit.text().strip()
        password1 = self.parol_edit.text().strip()
        password2 = self.parol2_edit.text().strip()
        if not name or not surname or not login or not password1 or not password2:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please fill all fields')
            return
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, surname, login, password1, password2])
        QtWidgets.QMessageBox.information(self, 'Information', 'User data has been saved successfully')


app = QtWidgets.QApplication(sys.argv)
registration_page = RegistrationPage()
registration_page.show()
sys.exit(app.exec())