
import unittest
import Complejos
import math

class TestMyModule(unittest.TestCase):
    
    def test_suma(self):
        a=(4,5)
        b=(4,6)
        self.assertEqual(Complejos.sumar(a, b), (8,11))
        
    def test_resta(self):
        a=(3,-2)
        b=(4,6)
        self.assertEqual(Complejos.restar(a, b), (-1,-8))

    def test_multiplicacion(self):
        a=(3,-2)
        b=(1,2)
        self.assertEqual(Complejos.multiplicar(a, b), (7,4))

    def test_modulo(self):
        a=(1,-1)
        self.assertEqual(Complejos.modulo(a), math.sqrt(2))

    def test_division(self):
        a=(-2,1)
        b=(1,2)
        self.assertEqual(Complejos.division(a, b), (0.0,1.0))

    def test_conjugado(self):
        a=(-2,1.032164)
        self.assertEqual(Complejos.conjugado(a), (-2,-1.032164))

    def test_cartesianoPolar(self):
        a=(1,1)
        self.assertEqual(Complejos.cartesianoPolar(a[0],a[1]), (math.sqrt(2),math.pi/4))

        
if __name__ == "__main__":
        unittest.main()
