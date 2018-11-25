from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow

import buddingStore
import mydata as database


class StoreWindow(QMainWindow):
    def __init__(self, callback):
        super(StoreWindow, self).__init__()
        self.callback = callback

    def closeEvent(self, event):
        self.callback()
        event.accept()


class StoreButton(QPushButton):
    def __init__(self, Text, controller, parent=None):
        super(StoreButton, self).__init__()
        self.window = StoreWindow(self.reverseState)
        self.store = buddingStore.BuddingStore(self.window, database.getItems(), controller)
        self.storeState = 0

    def mousePressEvent(self, QMouseEvent):
        if self.storeState == 0:
            self.window.show()
        else:
            self.window.close()
            self.reverseState()
        self.reverseState()

    def reverseState(self):
        self.storeState = 1 - self.storeState

    def tryClose(self):
        if self.storeState > 0:
            self.window.close()
