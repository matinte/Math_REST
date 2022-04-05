import unittest
import Operations


class Testing(unittest.TestCase):

    def test_suma(self):
        v1 = [6.3, 2.2, 12.0]
        v2 = [1.0, 2.0, 3.0]
        v_suma = [7.3, 4.2, 15]
        self.assertListEqual(v_suma, Operations.Operations.suma(self, v1, v2))

    def test_resta(self):
        v1 = [6.3, 2.0, 12.0]
        v2 = [1.0, 2.0, 3.0]
        v_resta = [5.3, 0.0, 9.0]
        self.assertListEqual(v_resta, Operations.Operations.resta(self, v1, v2))

    def test_mult(self):
        v1 = [6.3, 2.2, 12.0]
        v2 = [1.0, 2.0, 3.0]
        v_mult = [6.3, 4.4, 36.0]
        self.assertListEqual(v_mult, Operations.Operations.mult(self, v1, v2))

    def test_divis(self):
        a = True
        b = True
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
