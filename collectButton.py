from PyQt5.QtWidgets import *


class CollectButton(QPushButton):
    START_LABEL = "start smile!"
    STOP_LABEL = "collecting..."

    def __init__(self, Text, parent=None):
        super(CollectButton, self).__init__()
        self.state = False
        self.setText(self.START_LABEL)

    def enable(self):
        print("enableCollect")
        self.setEnabled(False)
        self.setText(self.STOP_LABEL)

    def disable(self):
        print("disableCollect")
        self.setEnabled(True)
        self.setText(self.START_LABEL)
