import unittest

from digital_cipher import *

class TestDigitalCipher(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode("scout",1939),[ 20, 12, 18, 30, 21])
        self.assertEqual(encode("kendy",1939),[12, 14, 17, 13, 26])
        self.assertEqual(encode("masterpiece",1939),[14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])
        self.assertEqual(encode("kendy",1985),[12, 14, 22, 9, 26])


    def test_decode(self):
        self.assertEqual(decode([ 20, 12, 18, 30, 21],1939),"scout")
        self.assertEqual(decode([12, 14, 17, 13, 26],1939),"kendy",)
        self.assertEqual(decode([ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8],1939),"masterpikece")
        self.assertEqual(decode([12, 14, 22, 9, 26],1985),"kendy")




if __name__ == '__main__':
    unittest.main()
