import unittest


def dzielenie(a,b):
    if b == 0:
        raise ValueError('Nie można dzielić przez 0')
    return a / b

class TestDzielenie(unittest.TestCase):
    def test_dzielenie_poprawne(self):
        self.assertEqual(dzielenie(10,2), 5)

    def test_dzielenie_przez_zero(self):
        with self.assertRaises(ValueError):
            dzielenie(1, 0)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDzielenie))