# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Главная2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1430, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Dob = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dob.setGeometry(QtCore.QRect(120, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Dob.setFont(font)
        self.pushButton_Dob.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Dob.setObjectName("pushButton_Dob")
        self.pushButton_Red = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Red.setGeometry(QtCore.QRect(610, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_Red.setFont(font)
        self.pushButton_Red.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Red.setObjectName("pushButton_Red")
        self.pushButton_Ydal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Ydal.setGeometry(QtCore.QRect(1040, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_Ydal.setFont(font)
        self.pushButton_Ydal.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Ydal.setObjectName("pushButton_Ydal")
        self.polosa2 = QtWidgets.QLabel(self.centralwidget)
        self.polosa2.setGeometry(QtCore.QRect(-20, 70, 1621, 20))
        self.polosa2.setObjectName("polosa2")
        self.polosa2_2 = QtWidgets.QLabel(self.centralwidget)
        self.polosa2_2.setGeometry(QtCore.QRect(-10, 120, 1621, 20))
        self.polosa2_2.setObjectName("polosa2_2")
        self.label_Tovar = QtWidgets.QLabel(self.centralwidget)
        self.label_Tovar.setGeometry(QtCore.QRect(580, 90, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tovar.setFont(font)
        self.label_Tovar.setObjectName("label_Tovar")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(-4, -8, 1431, 911))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Frame 5 (2).png"))
        self.label_9.setObjectName("label_9")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 190, 1241, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit_Poisk = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Poisk.setGeometry(QtCore.QRect(52, 149, 241, 31))
        self.lineEdit_Poisk.setObjectName("lineEdit_Poisk")
        self.pushButton_Poisk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Poisk.setGeometry(QtCore.QRect(300, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Poisk.setFont(font)
        self.pushButton_Poisk.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Poisk.setObjectName("pushButton_Poisk")
        self.label_9.raise_()
        self.pushButton_Dob.raise_()
        self.pushButton_Red.raise_()
        self.pushButton_Ydal.raise_()
        self.polosa2.raise_()
        self.polosa2_2.raise_()
        self.label_Tovar.raise_()
        self.tableWidget.raise_()
        self.lineEdit_Poisk.raise_()
        self.pushButton_Poisk.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Диафильмы"))
        self.pushButton_Dob.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_Red.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_Ydal.setText(_translate("MainWindow", "Удалить"))
        self.polosa2.setText(_translate("MainWindow", "___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.polosa2_2.setText(_translate("MainWindow", "___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.label_Tovar.setText(_translate("MainWindow", "Список Диафильмов"))
        self.pushButton_Poisk.setText(_translate("MainWindow", "Поиск"))
