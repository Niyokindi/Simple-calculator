import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(5, 9), 14)
        self.assertEqual(calculator.add(1, -1), 0)
        self.assertEqual(calculator.add(5, -9), -4)
        self.assertEqual(calculator.add(2.5, 1.3), 3.8)
        self.assertEqual(calculator.add(-2.5, 1.3), -3.8)


if __name__ == '__main__':
    unittest.main()
