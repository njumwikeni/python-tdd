#ship unit test

import unittest

from ship import *

class ShipTest (unittest.TestCase):
    def test_is_worth_it_false(self):
        self.assertIs(Ship(15,10).is_worth_it(),False)
    def test_is_worth_it_positive(self):
        self.assertIs(Ship(40,10).is_worth_it(),True)
if __name__ == '__main__':
    unittest.main()
