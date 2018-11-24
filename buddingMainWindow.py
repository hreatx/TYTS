# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file './buddingAction.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore
from PyQt5 import QtWidgets

import buddingWidget
import collectButton
import buddingController
import buddingMusic


# from PyQt5 import QtGui


class BuddingMainWindow(object):
    def __init__(self, user):
        self.controller = buddingController.BuddingController(self, user)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(0, 420)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth(),
        )
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth(),
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tittleWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tittleWidget.sizePolicy().hasHeightForWidth(),
        )
        self.tittleWidget.setSizePolicy(sizePolicy)
        self.tittleWidget.setObjectName("tittleWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tittleWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tittleLayout = QtWidgets.QHBoxLayout()
        self.tittleLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.tittleLayout.setObjectName("tittleLayout")
        self.money = QtWidgets.QLabel(self.tittleWidget)
        self.money.setObjectName("money")
        self.tittleLayout.addWidget(self.money)

        self.collectSmileButton = collectButton.CollectButton(
            self.tittleWidget,
        )
        self.collectSmileButton.setObjectName("collectSmileButton")

        self.tittleLayout.addWidget(self.collectSmileButton)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.tittleLayout.addItem(spacerItem)
        self.energy = QtWidgets.QLabel(self.tittleWidget)
        self.energy.setObjectName("energy")
        self.tittleLayout.addWidget(self.energy)
        self.level = QtWidgets.QLabel(self.tittleWidget)
        self.level.setObjectName("level")
        self.tittleLayout.addWidget(self.level)
        self.horizontalLayout_4.addLayout(self.tittleLayout)
        self.verticalLayout.addWidget(self.tittleWidget)
        self.contentWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.contentWidget.sizePolicy().hasHeightForWidth(),
        )
        self.contentWidget.setSizePolicy(sizePolicy)
        self.contentWidget.setObjectName("contentWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.contentWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.contentLayout = QtWidgets.QHBoxLayout()
        self.contentLayout.setObjectName("contentLayout")

        # left bound
        spacerItem1 = QtWidgets.QSpacerItem(
            0, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.contentLayout.addItem(spacerItem1)

        # add budding widget
        self.buddingWidget = buddingWidget.BuddingWidget(self.contentWidget, self.controller)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buddingWidget.sizePolicy().hasHeightForWidth(),
        )
        self.buddingWidget.setSizePolicy(sizePolicy)
        self.buddingWidget.setObjectName("buddingWidget")
        self.contentLayout.addWidget(self.buddingWidget)

        # right bound
        spacerItem2 = QtWidgets.QSpacerItem(
            0, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.contentLayout.addItem(spacerItem2)

        self.horizontalLayout_5.addLayout(self.contentLayout)
        self.verticalLayout.addWidget(self.contentWidget)
        self.tailWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tailWidget.sizePolicy().hasHeightForWidth(),
        )
        self.tailWidget.setSizePolicy(sizePolicy)
        self.tailWidget.setObjectName("tailWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tailWidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tailLayout = QtWidgets.QHBoxLayout()
        self.tailLayout.setObjectName("tailLayout")
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.tailLayout.addItem(spacerItem3)
        #self.voiceButton = QtWidgets.QPushButton(self.tailWidget)
        self.voiceButton = buddingMusic.BuddingVoice(self.tailWidget, self.controller)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.voiceButton.sizePolicy().hasHeightForWidth(),
        )
        self.voiceButton.setSizePolicy(sizePolicy)
        self.voiceButton.setObjectName("voiceButton")
        self.tailLayout.addWidget(self.voiceButton)
        self.storeButton = QtWidgets.QPushButton(self.tailWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.storeButton.sizePolicy().hasHeightForWidth(),
        )
        self.storeButton.setSizePolicy(sizePolicy)
        self.storeButton.setObjectName("storeButton")
        self.tailLayout.addWidget(self.storeButton)
        self.logoutButton = QtWidgets.QPushButton(self.tailWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.logoutButton.sizePolicy().hasHeightForWidth(),
        )
        self.logoutButton.setSizePolicy(sizePolicy)
        self.logoutButton.setObjectName("logoutButton")
        self.tailLayout.addWidget(self.logoutButton)
        self.horizontalLayout_6.addLayout(self.tailLayout)
        self.verticalLayout.addWidget(self.tailWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.makeConnection()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smile Budding!"))
        self.updateMoney(self.controller.money)
        self.energy.setText(_translate("MainWindow", "Energy"))
        self.level.setText(_translate("MainWindow", "Level"))
        self.voiceButton.setText(_translate("MainWindow", "voice"))
        self.storeButton.setText(_translate("MainWindow", "store"))
        self.logoutButton.setText(_translate("MainWindow", "logout"))

    def makeConnection(self):
        self.collectSmileButton.clicked.connect(self.controller.collect_start)
        pass

    def updateMoney(self, val):
        print("update money", val)
        self.money.setText("$" + str(val))

    def enableCollect(self):
        self.collectSmileButton.enable()

    def disableCollect(self, money):
        self.updateMoney(money)
        self.collectSmileButton.disable()
