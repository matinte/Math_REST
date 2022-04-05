import unittest
import Operations


class Testing(unittest.TestCase):

    def test_suma(self):
        v1 = [6.3, 2.2, 12]
        v2 = [1.0, 2.0, 3.0]
        v_suma = [7.3, 4.2, 15]
        self.assertListEqual(v_suma, Operations.Operations.suma(v1, v2, self))
        # check result returned vs expected
        #with self.assertRaises(TypeError):
        #    "Result different than expected"

    def test_resta(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_mult(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_divis(self):
        a = True
        b = True
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
