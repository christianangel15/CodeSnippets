from myargo import get_days_of_power
import unittest


class TestPower(unittest.TestCase):
    def test_Power(self):
        result = get_days_of_power(1000, 3, 500, 10, 1500, 7, 21000)
        result1 = get_days_of_power(
            R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
        result2 = get_days_of_power(
            R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
        result3 = get_days_of_power(
            R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)
        result4 = get_days_of_power(
            R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)
        self.assertEqual(result, 10)
        self.assertEqual(result1, 141)
        self.assertEqual(result2, 17)
        self.assertEqual(result3, 5)
        self.assertEqual(result4, 1)


if __name__ == '__main__':
    unittest.main()
