from buddingController import BuddingObserver


class BuddingTestObject(BuddingObserver):
    def on_level_update(self, level):
        print("BuddingTestObject level update!")
