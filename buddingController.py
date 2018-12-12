from PyQt5 import QtCore, QtWidgets

import buddingEmotion
import mydata as database
import time


# from PyQt5 import QtGui
# from PyQt5 import QtWidgets


class BuddingTestObject:
    def on_level_update(self, level):
        print("BuddingTestObject level update!")

    def on_logout(self, level):
        print("BuddingTestObject on_log_out!")


class BuddingCharacter:
    ENERGY_MAX = 100
    LEVEL_MAX = 3

    def __init__(self, energy=0, level=0):
        self.energy = energy
        self.level = level

    def set_energy_and_level(self, energy, level):
        self.energy = energy
        self.level = level

    def get_energy_and_level(self):
        return self.energy, self.level

    def add_energy(self, value, subject):
        # reset
        if value < 0:
            self.energy = 0
            if self.level > 0:
                self.level = 1
                if subject is not None:
                    subject.notify_all()
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
                if subject is not None:
                    subject.notify_all()
            return True


class BuddingPlayer:
    PENDING_MONEY = 10

    def __init__(self, user=None, money=0):
        self.user = user
        self.last_logout_time = -1
        if user is not None:
            self.last_logout_time = database.lastLogout(user)
            print("current user is", self.user, "last logout time is", self.last_logout_time)
            if self.last_logout_time is None:
                self.last_logout_time = -1

        self.money = money
        self.login_time = int(time.time())

    def get_user(self):
        return self.user

    def set_money(self, money):
        self.money = money

    def get_money(self):
        return self.money

    def increase_money(self, trans=PENDING_MONEY):
        self.money += trans

    def decrease_money(self, trans=PENDING_MONEY):
        if self.money >= trans:
            self.money -= trans
        else:
            self.money = 0

    def timeout(self):
        if self.last_logout_time < 0:
            return 0
        timeout = self.login_time - self.last_logout_time
        print("timeout", timeout, "detected!")
        return timeout

    # for logout
    def save_state(self):
        logout_time = int(time.time())
        print("save login", self.login_time, " logout", logout_time)
        database.record(self.user, self.login_time, logout_time)

    def get_login_time(self):
        return self.login_time


class BuddingController:
    COLLECT_TIME = 3000
    LOGIN_TIMEOUT = 100

    def __init__(self, ui=None, user=None, main_window=None):
        self.main_window = main_window
        self.budding = BuddingCharacter()
        self.player = BuddingPlayer(user)

        if ui is not None:
            self.ui = ui
            self.emotion = buddingEmotion.BuddingEmotion(self)
            self.load_state(user)

        self.observer_dict = {}
        # set level to zero

        timeout = self.player.timeout()

        if timeout > self.LOGIN_TIMEOUT:
            message = "Long time no play (" + str(timeout) + " seconds), reset all!"
            QtWidgets.QMessageBox.information(self.main_window, "info", message)
            self.budding.add_energy(-1, None)
        else:
            message = str(timeout) + " seconds since last play!"
            QtWidgets.QMessageBox.information(self.main_window, "info", message)

    def load_state(self, user):
        res = database.load(user)
        self.player.set_money(money=res[1])
        self.budding.set_energy_and_level(energy=res[2], level=res[3])

    def update_state(self):
        money = self.player.get_money()
        energy, level = self.budding.get_energy_and_level()
        self.ui.updateMoney(money)
        self.ui.updateEnergyAndLevel(energy, level)

    def collect_start(self):
        print("collect start")
        QtCore.QTimer().singleShot(self.COLLECT_TIME, self.collect_finish)
        self.ui.enableCollect()
        self.emotion.startRecog()

    def collect_finish(self):
        print("collect finish")
        money = self.player.get_money()
        self.ui.disableCollect(money)
        self.emotion.stopRecog()

        # save result to the database
        user = self.player.get_user()
        energy, level = self.budding.get_energy_and_level()
        database.save(user, money, energy, level)

    def on_success_event(self):
        self.player.increase_money()

    def on_fail_event(self):
        self.player.decrease_money()

    def set_item(self, money, energy):
        if money > self.player.get_money():
            return False
        if self.budding.add_energy(energy, self):
            self.player.decrease_money(money)
            self.update_state()
            return True
        else:
            return False

    def register_observer(self, name, observer):
        self.observer_dict[name] = observer

    def unregister_observer(self, name):
        del self.observer_dict[name]

    def notify_all(self):
        print("notify all")
        _, level = self.budding.get_energy_and_level()
        for k, v in self.observer_dict.items():
            print("notify name" + k)
            v.on_level_update(level)

    def get_level(self):
        _, level = self.budding.get_energy_and_level()
        return level

    def get_money(self):
        money = self.player.get_money()
        return money


# for test
if __name__ == '__main__':
    controller = BuddingController()

    testObject = BuddingTestObject()
    controller.register_observer('a', testObject)

    controller.budding.add_energy(200, controller)
