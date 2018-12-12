import time

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtPrintSupport import QPrinter

import mydata


class ReportButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, controller=None):
        super(ReportButton, self).__init__(parent)
        self.report = BuddingReport(controller)
        self.clicked.connect(self.report.save_to_pdf)


class BuddingReport:
    HEIGHT = 20

    def __init__(self, controller):
        self.controller = controller

    def save_to_pdf(self):
        user = self.controller.player.user
        login_time = self.controller.player.get_login_time()
        filename = "report_" + str(user) + "_" + str(int(time.time())) + ".pdf"
        printer = QPrinter()

        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        painter = QtGui.QPainter()
        painter.begin(printer)
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont('Decorative', 10))

        msg_list = []
        msg_list.append("Report for username " + user + "\n")

        msg_list.append("CurrentMoney " + str(self.controller.player.get_money()) + "\n")
        energy, level = self.controller.budding.get_energy_and_level()
        msg_list.append("Energy " + str(energy) + " ,Level " + str(level) + "\n")

        current_time = int(time.time() - login_time)
        msg_list.append("Current play time (seconds) " + str(current_time) + "\n")

        past_time = mydata.totalTime(user)

        total_time = int(current_time + past_time)
        msg_list.append("Play time in total (seconds) " + str(total_time) + "\n")

        start = 0
        end = self.HEIGHT
        for msg in msg_list:
            painter.drawText(QRect(0, start, 200, end), Qt.AlignLeft, msg)
            start = end
            end += self.HEIGHT
        painter.end()
