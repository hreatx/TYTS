from PyQt5 import QtCore

import abc
import buddingEmotion
import mydata as database
import buddingTestObject


# from PyQt5 import QtGui
# from PyQt5 import QtWidgets
class BuddingObserver(abc.ABC):
    @abc.abstractmethod
    def on_level_update(self, level):
        pass


class BuddingController:
    COLLECT_TIME = 3000
    PENDING_MONEY = 10
    ENERGY_MAX = 100

    def __init__(self, ui=None, user=None):
        if ui is not None:
            self.ui = ui
            self.emotion = buddingEmotion.BuddingEmotion(self)
            self.user = user
            print("current user is", self.user)
            res = database.load(self.user)
            print(res)
            self.money = res[1]
            self.energy = res[2]
            self.level = res[3]
        else:
            self.money = 0
            self.energy = 0
            self.level = 0
        self.observer_dict = {}

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
        self.change_energy(energy)

    def change_energy(self, value):
        self.energy += value
        self.state_handler()

    def state_handler(self):
        # update
        if self.energy >= self.ENERGY_MAX:
            self.energy -= self.ENERGY_MAX
            self.notify_all()

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

    testObject = buddingTestObject.BuddingTestObject()
    controller.register_observer('a', testObject)

    controller.change_energy(200)
