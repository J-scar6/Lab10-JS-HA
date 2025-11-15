import unittest
class TestCalculator(unittest.TestCase):

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,3,), 15)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(0, 888), 0)

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
        self.assertEqual(square_root(2), math.sqrt(2))





if __name__ == "__main__":
    unittest.main()

from calculator import *