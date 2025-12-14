import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()

    def test_float(self):
        self.assertAlmostEqual(self.calc.hitung_diskon(999, 33), 669.33, places=2)

    def test_harga_nol(self):
        self.assertEqual(self.calc.hitung_diskon(0, 50), 0)

if __name__ == "__main__":
    unittest.main()
