from PyQt5 import QtCore

import buddingEmotion
import mydata as database


# from PyQt5 import QtGui
# from PyQt5 import QtWidgets


class BuddingTestObject:
    def on_level_update(self, level):
        print("BuddingTestObject level update!")

    def on_logout(self, level):
        print("BuddingTestObject on_log_out!")


class BuddingController:
    COLLECT_TIME = 3000
    PENDING_MONEY = 10
    ENERGY_MAX = 100
    LEVEL_MAX = 3

    def __init__(self, ui=None, user=None):
        if ui is not None:
            self.ui = ui
            self.emotion = buddingEmotion.BuddingEmotion(self)
            self.user = user
            print("current user is", self.user)
            self.load_state()
        else:
            self.money = 0
            self.energy = 0
            self.level = 0
        self.observer_dict = {}

    def load_state(self):
        res = database.load(self.user)
        self.money = res[1]
        self.money = 500
        self.energy = res[2]
        self.level = res[3]

    def update_state(self):
        self.ui.updateMoney(self.money)
        self.ui.updateEnergyAndLevel(self.energy, self.level)

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
        if self.add_energy(energy):
            self.money -= money
            self.update_state()
            return True
        else:
            return False

    def add_energy(self, value):
        # reset
        if value < 0:
            self.energy = 0
            if self.level > 0:
                self.level = 0
                self.notify_all()
                return True
        else:
            self.energy += value
            if self.level == self.LEVEL_MAX:
                if self.energy <= self.ENERGY_MAX:
                    return True
                else:
                    self.energy -= value
                    return False

            # upgrade
            if self.energy >= self.ENERGY_MAX:
                while self.energy >= self.ENERGY_MAX:
                    self.energy -= self.ENERGY_MAX
                    if self.level < self.LEVEL_MAX:
                        self.level += 1
                if self.level > self.LEVEL_MAX:
                    self.level = self.LEVEL_MAX
                self.notify_all()
            return True

    def register_observer(self, name, observer):
        self.observer_dict[name] = observer

    def unregister_observer(self, name):
        del self.observer_dict[name]

    def notify_all(self):
        print("notify all")
        for k, v in self.observer_dict.items():
            print("notify name" + k)
            v.on_level_update(self.level)

    def get_level(self):
        return self.level

    def get_money(self):
        return self.money


if __name__ == '__main__':
    controller = BuddingController()

    testObject = BuddingTestObject()
    controller.register_observer('a', testObject)

    controller.add_energy(200)
