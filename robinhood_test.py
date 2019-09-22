import unittest

from robinhood import *

class DragonTest (unittest.TestCase):
    def test_can_survive(self):
        self.assertTrue(can_survive(20,8),True)
        self.assertFalse(can_survive(2,8),False)
        self.assertTrue(can_survive(20,10),True)
        self.assertFalse(can_survive(8,8),False)



if __name__ == '__main__':
    unittest.main()
