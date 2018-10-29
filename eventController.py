from PyQt5 import QtCore

import buddingEmotion
import mydata as database
# from PyQt5 import QtGui
# from PyQt5 import QtWidgets


class EventController:
    COLLECT_TIME = 3000
    PENDING_MONEY = 10

    def __init__(self, ui, user):
        self.ui = ui
        self.emotion = buddingEmotion.BuddingEmotion(self)
        self.user = user
        print("current user is", self.user)
        res = database.load(self.user)
        print(res)
        self.money = res[1]
        self.energy = res[2]
        self.level = res[3]

    def collectStart(self):
        print("collect start")
        QtCore.QTimer().singleShot(self.COLLECT_TIME, self.collectFinish)
        self.ui.enableCollect()
        self.emotion.startRecog()

    def collectFinish(self):
        print("collect finish")
        self.ui.disableCollect(self.money)

        self.emotion.stopRecog()
        database.save(self.user, self.money, self.energy, self.level)

    def onSuccessEvent(self):
        self.money += self.PENDING_MONEY

    def onFailEvent(self):
        if self.money >= self.PENDING_MONEY:
            self.money -= self.PENDING_MONEY
        else:
            self.money = 0
