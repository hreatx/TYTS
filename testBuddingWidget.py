import unittest
import sys
sys.path.append('../')
import buddingWidget


class BuddingWidgetMock(buddingWidget.BuddingWidget):

    def __init__(self):
        self.totalMovieSize = 0
        self.currentMovieIndex = 0

    def getNextMovie(self):
        """
        Adapt the original method of BuddingWidgetMock by removing its dependency on other object so that
        we only run unit test on its code used for calculation.
        """
        self.currentMovieIndex += 1
        if self.currentMovieIndex == self.totalMovieSize:
            self.currentMovieIndex = 0


class TestBuddingWidget(unittest.TestCase):

    def setUp(self):
        self.widget = BuddingWidgetMock()

    def testHetNextMovie(self):
        self.widget.getNextMovie()
        self.widget.totalMovieSize = 6
        self.widget.currentMovieIndex = 0

        for i in range(6): # if currentMovieIndex == totalMovieSize it should set totalMovieSize to 0
            self.widget.getNextMovie()

        print(self.widget.currentMovieIndex)
        self.assertEqual(self.widget.currentMovieIndex, 0)


if __name__ == "__main__":
    unittest.main()


