from unittest import TestCase
import canculator
import math

class TestAdd(TestCase):

    def test_001(self):
        self.assertEqual(canculator.add(2, 3), 5)

    def test_002(self):
        self.assertEqual(canculator.subtract(6, 3), 3)

    def test_003(self):
        self.assertEqual(canculator.multiply(4, 3), 12)

    def test_004(self):
        self.assertEqual(canculator.divide(100, 10), 10)

    def test_005(self):
        self.assertEqual(canculator.exponentiation(10, 2), 100)

    def test_006(self):
        self.assertEqual(canculator.sqrt(144), 12)

    def test_007(self):
        self.assertEqual(canculator.percentage(60, 20), 12)