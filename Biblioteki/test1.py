import unittest

def suma(a,b):
    return a + b

class TestSum(unittest.TestCase):

    def test_suma_dodatnich(self):
        self.assertEqual(suma(2,2),4)
        self.assertNotEqual(suma(2,3),7)
    def test_suma_ujemnych(self):
        self.assertEqual(suma(-2,-2),-4)
        self.assertEqual(suma(-2,-3),-5)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestSum))