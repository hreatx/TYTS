import time

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtPrintSupport import QPrinter


class ReportButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, user=None):
        super(ReportButton, self).__init__(parent)
        self.report = BuddingReport(user)
        self.clicked.connect(self.report.save_to_pdf)


class BuddingReport:
    def __init__(self, user):
        self.user = user

    def save_to_pdf(self):
        filename = "player_report/report_" + str(self.user) + "_" + str(int(time.time())) + ".pdf"
        printer = QPrinter()

        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        painter = QtGui.QPainter()
        painter.begin(printer)
        painter.setPen(QColor(168, 34, 3))
        painter.setFont(QFont('Decorative', 10))
        painter.drawText(QRect(0, 0, 100, 100), Qt.AlignCenter, "this is a test2")
        painter.end()
