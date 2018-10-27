import buddingEmotion
import databaseMock

from PyQt5 import QtCore, QtGui, QtWidgets


class EventController:
    COLLECT_TIME = 3000
    PENDING_MONEY = 10

    def __init__(self, ui):
        self.ui = ui
        self.emotion = buddingEmotion.BuddingEmotion(self)
        self.database = databaseMock.DatabaseMock()
        self.userName = "admin"
        self.money, self.energy, self.level = self.database.load(self.userName)

    def collectStart(self):
        print("collect start")
        QtCore.QTimer().singleShot(self.COLLECT_TIME, self.collectFinish)
        self.ui.enableCollect()
        self.emotion.startRecog()

    def collectFinish(self):
        print("collect finish")
        self.ui.disableCollect(self.money)
        self.emotion.stopRecog()

    def onSuccessEvent(self):
        self.money += self.PENDING_MONEY

    def onFailEvent(self):
        if self.money >= self.PENDING_MONEY:
            self.money -= self.PENDING_MONEY
        else:
            self.money = 0
