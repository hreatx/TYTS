import unittest

import buddingController
from buddingController import BuddingController


class buddingControllerMocker(BuddingController):
    """
    Inherit the EventController in order to mock it without calling the database.
    Inspired by: https://stackoverflow.com/questions/17836939/mocking-init-for-unittesting
    """

    def __init__(self, money):
        self.money = money

    # mock the increase and decrease method from Player class directly here. This avoid calling the database.
    def increase_money(self, trans):
        self.money += trans

    def decrease_money(self, trans):
        if self.money >= trans:
            self.money -= trans
        else:
            self.money = 0


class TestEventController(unittest.TestCase):

    def setUp(self):

        self.controller = buddingControllerMocker(0)

    def testIncreaseMoney(self):  # increase money, equivalent class A
        self.controller.increase_money(10)
        self.assertEqual(self.controller.money, 10)

    def testDeductMoney(self):  # deduct money, equivalent class A
        self.controller.decrease_money(10)
        self.assertEqual(self.controller.money, 0)

    def testMoneyBelowZero(self):  # money cannot below zero, equivalent class B
        self.controller.decrease_money(10)
        self.assertEqual(self.controller.money, 0)


if __name__ == "__main__":

    unittest.main()
