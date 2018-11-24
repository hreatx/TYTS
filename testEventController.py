import unittest

from buddingController import BuddingController


class buddingControllerMocker(BuddingController):
    """
    Interit the EventController in order to mock it without calling the database.
    Inspired by: https://stackoverflow.com/questions/17836939/mocking-init-for-unittesting
    """

    def __init__(self, money):
        self.money = money


class TestEventController(unittest.TestCase):

    def setUp(self):

        self.controller = buddingControllerMocker(0)

    def testIncreaseMoney(self):  # increase money, equivalent class A
        self.controller.money = 0
        self.controller.on_success_event()
        self.assertEqual(self.controller.money, 10)

    def testDeductMoney(self):  # deduct money, equivalent class A
        self.controller.money = 10
        self.controller.on_fail_event()
        self.assertEqual(self.controller.money, 0)

    def testMoneyBelowZero(self):  # money cannot below zero, equivalent class B
        self.controller.money = 0
        self.controller.on_fail_event()
        self.assertEqual(self.controller.money, 0)


if __name__ == "__main__":

    unittest.main()
