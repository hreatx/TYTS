import copy
import os
import sys

from PyQt5 import QtWidgets

import mydata
from buddingMainWindow import BuddingMainWindow
from login_window import Ui_Login_Window


class ApplicationWindow(QtWidgets.QMainWindow):
    def test_clicked(self):
        self.ui.mylab.setText(str(self.i))
        self.i += 1

    def login_clicked(self):
        self.user = copy.copy(self.ui.username.text())
        self.pwd = copy.copy(self.ui.pwd.text())
        self.ui.pwd.setText("")
        self.ui.username.setText("")
        if len(self.user) == 0 or len(self.pwd) == 0:
            QtWidgets.QMessageBox.critical(self, "error", "Enter something!")
            return

        if not mydata.login(self.user, self.pwd):
            QtWidgets.QMessageBox.critical(
                self, "error", "username doesn't exist or wrong password!",
            )
            return

        QtWidgets.QMessageBox.information(
            self, "warining", "username: %s\npassword: %s\n" % (
                self.user, self.pwd,
            ),
        )
        self.change_clicked()

    def reg_clicked(self):
        self.user = copy.copy(self.ui.username.text())
        self.pwd = copy.copy(self.ui.pwd.text())
        self.ui.pwd.setText("")
        self.ui.username.setText("")
        if len(self.user) == 0 or len(self.pwd) == 0:
            QtWidgets.QMessageBox.critical(self, "error", "Enter something!")
            return

        if mydata.check(self.user):
            QtWidgets.QMessageBox.critical(
                self, "error", "username already exists!!",
            )
            return
        mydata.register(self.user, self.pwd)

        QtWidgets.QMessageBox.information(
            self, "cong", "username: %s\npassword: %s\ncreated!" % (
                self.user, self.pwd,
            ),
        )

    def change_clicked(self):
        self.other = BuddingWindow(self.user)
        self.other.user = self.user
        self.other.other = self
        self.close()
        print("user %s login" % (self.user))
        self.other.show()

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.user = None
        self.pwd = None
        self.i = 0
        self.other = None
        self.ui = Ui_Login_Window()
        self.ui.setupUi(self)
        self.ui.reg.clicked.connect(self.reg_clicked)
        self.ui.login.clicked.connect(self.login_clicked)
        self.ui.test.clicked.connect(self.test_clicked)
        self.ui.change.clicked.connect(self.change_clicked)


class BuddingWindow(QtWidgets.QMainWindow):
    def __init__(self, user, parent=None):
        self.val = 0
        super(BuddingWindow, self).__init__(parent)
        self.ui = BuddingMainWindow(user, self)
        self.other = None
        self.user = None
        self.pwd = None

        self.ui.logoutButton.clicked.connect(self.logout_clicked)

    def logout_clicked(self):
        self.close()
        self.other.show()

    def closeEvent(self, event):
        self.ui.tryCloseStore()
        event.accept()


def start():
    if not os.path.exists('mydata.db'):
        mydata.initDB()

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
