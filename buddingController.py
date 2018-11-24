from PyQt5 import QtCore

import buddingEmotion
import mydata as database


# from PyQt5 import QtGui
# from PyQt5 import QtWidgets

class BuddingController:
    COLLECT_TIME = 3000
    PENDING_MONEY = 10
    COLLECT_ENERGY = 100

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

    def collect_start(self):
        print("collect start")
        QtCore.QTimer().singleShot(self.COLLECT_TIME, self.collect_finish)
        self.ui.enableCollect()
        self.emotion.startRecog()

    def collect_finish(self):
        print("collect finish")
        self.ui.disableCollect(self.money)

        self.emotion.stopRecog()
        database.save(self.user, self.money, self.energy, self.level)

    def on_success_event(self):
        self.money += self.PENDING_MONEY

    def on_fail_event(self):
        if self.money >= self.PENDING_MONEY:
            self.money -= self.PENDING_MONEY
        else:
            self.money = 0

    def set_item(self, money, energy):
        if money > self.money:
            return False

        self.money -= money
        self.energy += energy
        self.state_handler()

    def state_handler(self):
        pass

    def get_level(self):
        return self.level

    def get_money(self):
        return self.money
