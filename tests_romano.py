import unittest
from romano import Romano


class RomanoTest(unittest.TestCase):

    # Testes classe invalida
    def test_romano01(self):
        c = "XXXXOVI"
        self.assertEqual(Romano.convert_romano(c), None)

    def test_romano02(self):
        c = "CCCCII"
        self.assertEqual(Romano.convert_romano(c), None)

    def test_romano03(self):
        c = "UIJ"
        self.assertEqual(Romano.convert_romano(c), None)

    # Testes de classe valida
    def test_romano04(self):
        c = "CCXIV"
        self.assertEqual(Romano.convert_romano(c), 214)

    def test_romano05(self):
        c = "XXII"
        self.assertEqual(Romano.convert_romano(c), 22)

    def test_romano06(self):
        c = "LIV"
        self.assertEqual(Romano.convert_romano(c), 54)

    def test_romano07(self):
        c = "MDIV"
        self.assertEqual(Romano.convert_romano(c), 1504)

    def test_romano08(self):
        c = "MMDIX"
        self.assertEqual(Romano.convert_romano(c), 2509)
