import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_widget import Ui_Widget
import cv2

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Widget()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())