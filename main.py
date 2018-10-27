import sys
import os
from PyQt5.QtWidgets import *
import buddingMainWindow


class BuddingMainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.val = 0
        super(BuddingMainWindow, self).__init__(parent)
        self.ui = buddingMainWindow.BuddingMainWindow()
        self.ui.setupUi(self)
        self.user = None
        self.pwd = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = BuddingMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
