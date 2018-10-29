# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


class Ui_Login_Window(object):
    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.resize(592, 448)
        self.centralWidget = QtWidgets.QWidget(Login_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(90, 120, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 71, 16))
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.centralWidget)
        self.username.setGeometry(QtCore.QRect(200, 120, 211, 21))
        self.username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username.setObjectName("username")
        self.pwd = QtWidgets.QLineEdit(self.centralWidget)
        self.pwd.setGeometry(QtCore.QRect(200, 190, 211, 21))
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(230, 30, 221, 21))
        self.label_3.setObjectName("label_3")
        self.reg = QtWidgets.QPushButton(self.centralWidget)
        self.reg.setGeometry(QtCore.QRect(130, 270, 114, 32))
        self.reg.setObjectName("reg")
        self.login = QtWidgets.QPushButton(self.centralWidget)
        self.login.setGeometry(QtCore.QRect(320, 270, 114, 32))
        self.login.setObjectName("login")
        self.test = QtWidgets.QPushButton(self.centralWidget)
        self.test.setGeometry(QtCore.QRect(130, 320, 114, 32))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.test.sizePolicy().hasHeightForWidth(),
        )
        self.test.setSizePolicy(sizePolicy)
        self.test.setObjectName("test")
        self.mylab = QtWidgets.QLabel(self.centralWidget)
        self.mylab.setGeometry(QtCore.QRect(440, 150, 59, 16))
        self.mylab.setObjectName("mylab")
        self.change = QtWidgets.QPushButton(self.centralWidget)
        self.change.setGeometry(QtCore.QRect(320, 320, 114, 32))
        self.change.setObjectName("change")
        Login_Window.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Login_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 592, 22))
        self.menuBar.setObjectName("menuBar")
        Login_Window.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Login_Window)
        self.mainToolBar.setObjectName("mainToolBar")
        Login_Window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Login_Window)
        self.statusBar.setObjectName("statusBar")
        Login_Window.setStatusBar(self.statusBar)

        self.retranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "MainWindow"))
        self.label.setText(_translate("Login_Window", "Username"))
        self.label_2.setText(_translate("Login_Window", "Password"))
        self.label_3.setText(_translate("Login_Window", "Smiley Budding!"))
        self.reg.setText(_translate("Login_Window", "Register"))
        self.login.setText(_translate("Login_Window", "Login"))
        self.test.setText(_translate("Login_Window", "test"))
        self.mylab.setText(_translate("Login_Window", "0"))
        self.change.setText(_translate("Login_Window", "change"))
