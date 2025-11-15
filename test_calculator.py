import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,3,), 15)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(0, 888), 0)

    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-5,3),-2)
        self.assertEqual(add(0,10),10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,2),3)
        self.assertEqual(sub(-1,-1),0)
        self.assertEqual(sub(0,9),-9)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,10,), 5)
        self.assertEqual(div(2,15,), 7.5)
        self.assertEqual(div(-4,8,), -2)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4), 5.0)
        self.assertAlmostEqual(hypotenuse(5,12), 13.0)
        self.assertAlmostEqual(hypotenuse(0,0), 0.0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument:
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(1), 1)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

    def test_divide_by_zero(self):# 1 assertion
        try:
            div(5,0)
            assert False, "Expected ZeroDivisionError"
        except ZeroDivisionError:
            pass

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10,100),2)
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(3, 27), 3)

    def test_log_invalid_base(self): # 1 assertion
        try:
            log(1,5)
            assert False, "Expected ValueError"
        except ValueError:
            pass

if __name__ == "__main__":
    unittest.main()

