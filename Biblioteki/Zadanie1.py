import math
import unittest

class Kalkulator:
    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def roznica(a, b):
        return a - b

    @staticmethod
    def mnozenie(a, b):
        return a * b

    @staticmethod
    def dzielenie(a, b):
        return a / b

    @staticmethod
    def pierwiastek(a):
        return  math.sqrt(a)

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_suma_dodatnich(self):
        self.assertEqual(self.kalkulator.suma(2,2),4)
        self.assertNotEqual(self.kalkulator.suma(2,3),7)
    def test_suma_ujemnych(self):
        self.assertEqual(self.kalkulator.roznica(-2,2),-4)
        self.assertEqual(self.kalkulator.roznica(-2,1),-3)
    def test_mnozenie(self):
        self.assertEqual(self.kalkulator.mnozenie(2,2),4)
        self.assertNotEqual(self.kalkulator.mnozenie(2,4),6)
    def test_dzielenie(self):
        self.assertEqual(self.kalkulator.dzielenie(10, 2),5)
        self.assertEqual(self.kalkulator.dzielenie(20, 5),4)
    def test_pierwiastek(self):
        self.assertEqual(self.kalkulator.pierwiastek(9), 3)
        self.assertEqual(self.kalkulator.pierwiastek(81), 9)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestKalkulator))