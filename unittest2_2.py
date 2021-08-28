from unittest import TestCase
import canculator
import math

class TestAdd(TestCase):

    def test_add_1(self):
        self.assertEqual(canculator.add(2, 3), 5)

    def test_add_2(self):
        self.assertNotEqual(canculator.add(12, 4), 7)

    def test_sub_1(self):
        self.assertEqual(canculator.subtract(6, 3), 3)

    def test_sub_2(self):
        self.assertNotEqual(canculator.subtract(14, 8), 31)

    def test_miul_01(self):
        self.assertEqual(canculator.multiply(4, 3), 12)

    def test_mul_02(self):
        self.assertNotEqual(canculator.multiply(7, 5), 111)

    def test_div_01(self):
        self.assertEqual(canculator.divide(100, 10), 10)

    def test_div_02(self):
        with self.assertRaises(ZeroDivisionError):
            canculator.divide(10, 0)

    def test_ex_1(self):
        self.assertEqual(canculator.exponentiation(10, 2), 100)

    def test_ex_2(self):
        self.assertTrue(canculator.exponentiation(10, 2), 100)

    def test_sqrt_1(self):
        self.assertEqual(canculator.sqrt(144), 12)

    def test_sqrt_2(self):
        self.assertNotEqual(canculator.sqrt(221), 2)

    def test_per_1(self):
        self.assertEqual(canculator.percentage(60, 20), 12)

    def test_per_2(self):
        self.assertIsInstance(canculator.percentage(100, 8), float)