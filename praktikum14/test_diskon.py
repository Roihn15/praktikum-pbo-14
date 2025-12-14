import unittest
from diskon_service import DiskonCalculator

class TestDiskon(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()

    def test_diskon_normal(self):
        self.assertEqual(self.calc.hitung_diskon(1000, 10), 900)

    def test_diskon_100_persen(self):
        self.assertEqual(self.calc.hitung_diskon(1000, 100), 0)

    def test_diskon_0_persen(self):
        self.assertEqual(self.calc.hitung_diskon(1000, 0), 1000)

if __name__ == "__main__":
    unittest.main()
