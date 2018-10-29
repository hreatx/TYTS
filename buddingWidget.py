import os

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

dir = os.path.dirname(os.path.abspath(__file__))


class BuddingWidget(QWidget):

    def __init__(self, parent):
        super(BuddingWidget, self).__init__(parent)

        self.currentMovieIndex = -1
        self.totalMovieSize = 5

        self.layout = QHBoxLayout(self)
        self.movieLabel = QLabel(self)
        self.showNextMovie()
        self.layout.addWidget(self.movieLabel)
        self.setLayout(self.layout)

    def mousePressEvent(self, event):
        print("pressed")
        self.showNextMovie()

    def showNextMovie(self):
        movie = self.getNextMovie()
        movie.setScaledSize(QSize(200, 200))
        self.movieLabel.setMovie(movie)
        movie.start()

    def mouseReleaseEvent(self, event):
        print("released")

    def getNextMovie(self):
        self.currentMovieIndex += 1
        if self.currentMovieIndex == self.totalMovieSize:
            self.currentMovieIndex = 0
        filename = "test_" + str(self.currentMovieIndex) + ".gif"
        return QMovie(os.path.join(dir, filename))
