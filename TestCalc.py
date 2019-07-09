import unittest
from calc import *

class TestCalc(unittest.TestCase):

    def  testadd(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)


    def testsub(self):
        result = calc.substract(30,5)
        self.assertEqual(result,24)


if __name__ == "__main__":
        unittest.main()