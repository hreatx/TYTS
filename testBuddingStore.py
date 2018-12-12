import unittest


class BuddingStoreMock(object):
    COLLECT_TIME = 3000
    PENDING_MONEY = 10
    ENERGY_MAX = 100
    LEVEL_MAX = 3

    def __init__(self):
        self.totalMovieSize = 0
        self.currentMovieIndex = 0
        self.money = 0
        self.energy = 0
        self.level = 0

    def add_energy(self, value):
        # reset
        if value < 0:
            self.energy = 0
            if self.level > 0:
                self.level = 0
                # self.notify_all()
                return True
        else:
            self.energy += value
            if self.level == self.LEVEL_MAX:
                if self.energy <= self.ENERGY_MAX:
                    return True
                else:
                    self.energy -= value
                    return False

            # upgrade
            if self.energy >= self.ENERGY_MAX:
                while self.energy >= self.ENERGY_MAX:
                    self.energy -= self.ENERGY_MAX
                    if self.level < self.LEVEL_MAX:
                        self.level += 1
                if self.level > self.LEVEL_MAX:
                    self.level = self.LEVEL_MAX
                # self.notify_all()
            return True

    def set_item(self, money, energy):
        if money > self.money:
            return False
        if self.add_energy(energy):
            self.money -= money
            # self.update_state()
            return True
        else:
            return False


class TestBuddingBudding(unittest.TestCase):

    def setUp(self):
        self.widget = BuddingStoreMock()

    # test add energy
    def test_add_energy1(self):
        self.widget.energy = 0
        self.widget.add_energy(10)
        self.assertEqual(self.widget.energy, 10)

    # test reduce energy
    def test_add_energy3(self):
        self.widget.energy = 10
        self.widget.add_energy(-10)
        self.assertEqual(self.widget.energy, 0)

    # energy cannot be smaller than 0
    def test_add_energy2(self):
        self.widget.energy = 0
        self.widget.add_energy(-10)
        self.assertEqual(self.widget.energy, 0)

    # level 3 with large energy
    def test_level_up(self):
        self.widget.energy = 0
        self.widget.level = 0
        self.widget.add_energy(10000)
        self.assertEqual(self.widget.level, 3)

    # level 1
    def test_level_up2(self):
        self.widget.energy = 0
        self.widget.level = 0
        self.widget.add_energy(100)
        self.assertEqual(self.widget.level, 1)

    # level 2
    def test_level_up3(self):
        self.widget.energy = 0
        self.widget.level = 0
        self.widget.add_energy(200)
        self.assertEqual(self.widget.level, 2)


    # test affordable purchase
    def test_purchase(self):
        self.widget.energy = 0
        self.widget.level = 0
        self.widget.money = 500

        self.widget.set_item(money=50, energy=0)

        self.assertEqual(self.widget.money, 450)

    # test unaffordable purchase
    def test_purchase(self):
        self.widget.energy = 0
        self.widget.level = 0
        self.widget.money = 20

        self.assertFalse(self.widget.set_item(money=50, energy=0))

        self.assertEqual(self.widget.money, 20)

if __name__ == "__main__":
    unittest.main()


