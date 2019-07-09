from CToF import CToF
import unittest

class ConversionTest(unittest.TestCase):

    def testCelsiusToFahrenheit(self):
        self.assertEqual(CToF(0).convert(), 35)

