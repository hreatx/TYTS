# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rl/new/widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class BuddingStore:
    def __init__(self, storeWindow, itemList, controller):
        self.window = storeWindow
        self.controller = controller
        self.itemDict = {}
        self.buttons = {}
        self.setupUi(storeWindow, itemList)

    def setupUi(self, storeWindow, itemList):
        storeWindow.setObjectName("buddingStore")
        storeWindow.setEnabled(True)

        self.verticalLayoutWidget = QtWidgets.QWidget(storeWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 181, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        for item in itemList:
            self.itemDict[item['name']] = item
            self.buttons[item['name']] = QtWidgets.QPushButton(self.verticalLayoutWidget)
            self.buttons[item['name']].setObjectName(item['name'])
            self.buttons[item['name']].clicked.connect(lambda state, it=item: self.tryToBuy(it))
            self.verticalLayout.addWidget(self.buttons[item['name']])

        self.retranslateUi(storeWindow)

        storeWindow.resize(200, 300)

        QtCore.QMetaObject.connectSlotsByName(storeWindow)

    @staticmethod
    def item_to_string(item):
        return item['name'] + '\n' + 'price ' + str(item['price']) + \
               ' energy ' + str(item['energy'])

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("buddingStore", "buddingStore"))
        for k, v in self.buttons.items():
            v.setText(_translate("buddingStore", self.item_to_string(self.itemDict[k])))

    def tryToBuy(self, item):
        print(item)
        if not self.controller.set_item(item['price'], item['energy']):
            QtWidgets.QMessageBox.critical(self.window, "error", "not enough money")

