
import unittest
import Complejos
import math

class TestMyModule(unittest.TestCase):
    
    def test_suma(self):
        a=(4,5)
        b=(4,6)
        self.assertEqual(Complejos.sumar(a, b), (8,11))
        self.assertEqual(Complejos.sumar((3,-1), (1,4)), (4,3))
        
    def test_resta(self):
        a=(3,-2)
        b=(4,6)
        self.assertEqual(Complejos.restar(a, b), (-1,-8))

    def test_multiplicacion(self):
        a=(3,-2)
        b=(1,2)
        self.assertEqual(Complejos.multiplicar(a, b), (7,4))
        self.assertEqual(Complejos.multiplicar((3,-1), (1,4)), (7,11))
        self.assertEqual(Complejos.multiplicar((1,1), (-1,1)), (-2,0))

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
        self.assertEqual(Complejos.cartesianoPolar(a), (math.sqrt(2),math.pi/4))

    def test_polarCartesiano(self):
        a=(math.sqrt(2),math.pi/4)
        self.assertEqual(Complejos.polarCartesiano(a),(1,1))

    def test_fase(self):
        a=(4,4*math.sqrt(3))
        self.assertEqual(Complejos.fase(a),1.05)

    def test_sumaVectoresComplejos(self):
        a=[(6,-4),(7,3),(42,-81),(0,-3)]
        b=[(16,23),(0,-7),(6,0),(0,-4)]
        res=[(22,19),(7,-4),(48,-81),(0,-7)]
        self.assertEqual(Complejos.sumaVectoresComplejos(a,b),res)

    def test_inversaVectores(self):
        a=[(6,-4),(7,3),(42,-81),(0,-3)]
        res=[(-6,4),(-7,-3),(-42,81),(0,3)]
        self.assertEqual(Complejos.inversaVectores(a),res)

    def test_multEscalarVectores(self):
        a=(3,2)
        b=[(6,3),(0,0),(5,1),(4,0)]
        res=[(12,21),(0,0),(13,13),(12,8)]
        self.assertEqual(Complejos.multEscalarVectores(a,b),res)

    def test_sumaMatricesComplejas(self):
        a=[[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]
        b=[[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]]
        res=[[(8,2),(2,-1),(11,-10)],[(1,0),(8,7),(2,1)],[(11,-5),(2,7),(4,0)]]
        self.assertEqual(Complejos.sumaMatricesComplejas(a,b),res)
        res='No es posible hacer la suma de matrices, revisa las dimensinones.'
        b=[[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7)]]
        self.assertEqual(Complejos.sumaMatricesComplejas(a,b),res)

    def test_inversaMatricesComplejas(self):
        a=[[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)]]
        res=[[(-3,-2),(0,0),(-5,6)],[(-1,0),(-4,-2),(0,-1)]]
        self.assertEqual(Complejos.inversaMatricesComplejas(a),res)

    def test_multEscalarMatriz(self):
        a=[[(1,1),(1,1)],[(1,1),(-1,-1)]]
        r=(1/math.sqrt(2),0)
        res=[[(0.7071067811865475,0.7071067811865475),(0.7071067811865475, 0.7071067811865475)],[(0.7071067811865475,0.7071067811865475),(-0.7071067811865475,-0.7071067811865475)]]
        self.assertEqual(Complejos.multEscalarMatriz(r,a),res)

    def test_transpuestaMatriz(self):
        a=[[(1,1),(2,2),(3,3)]]
        res=[[(1,1)],[(2,2)],[(3,3)]]
        self.assertEqual(Complejos.transpuestaMatriz(a),res)

    def test_conjugadoMatriz(self):
        a=[[(1,1),(2,2),(3,3)]]
        res=[[(1,-1),(2,-2),(3,-3)]]
        self.assertEqual(Complejos.conjugadoMatriz(a),res)

    def test_adjuntaMatriz(self):
        a=[[(1,1),(2,2),(3,3)]]
        res=[[(1,-1)],[(2,-2)],[(3,-3)]]
        self.assertEqual(Complejos.adjuntaMatriz(a),res)
        
    def test_productoDeMatrices(self):
        a=[[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]
        b=[[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7),(0,0)]]
        res=[[(26,-52),(60,24),(26,0)],[(9,7),(1,29),(14,0)],[(48,-21),(15,22),(20,-22)]]
        self.assertEqual(Complejos.productoDeMatrices(a,b),res)
        b=[[(5,0),(2,-1),(6,-4)],[(0,0),(4,5),(2,0)],[(7,-4),(2,7)]]
        res='No es posible hacer el prudcto de matrices, revisa las dimensiones.'
        self.assertEqual(Complejos.productoDeMatrices(a,b),res)

    def test_productoMatrizVector(self):
        a=[[(2,0),(-3/2,0)],[(-3,0),(5/2,0)]]
        vec=[(3,0),(-2,0)]
        res=[(9,0),(-14,0)]
        self.assertEqual(Complejos.productoMatrizVector(a,vec),res)

    def test_productoInternoVectores(self):
        a=[(5,0),(3,0),(-7,0)]
        b=[(6,0),(2,0),(0,0)]
        res=(36,0)
        self.assertEqual(Complejos.productoInternoVectores(a,b),res)
        
    def test_normaVector(self):
        a=[(3,0),(-6,0),(2,0)]
        self.assertEqual(Complejos.normaVector(a),7)

    def test_distanciaVectores(self):
        a=[(3,0),(1,0),(2,0)]
        v=[(2,0),(2,0),(-1,0)]
        res=math.sqrt(11)
        self.assertEqual(Complejos.distanciaVectores(a,v),res)

    def test_matrizUnitariaComprobacion(self):
        r=1/math.sqrt(2)
        a=[[(0,r),(0,-r)],[(0,r),(0,r)]]
        self.assertEqual(Complejos.matrizUnitariaComprobacion(a),True)

    def test_matrizHermitianaComprobacion(self):
        a=[[(-1,0),(0,-1)],[(0,1),(1,0)]]
        self.assertEqual(Complejos.matrizHermitianaComprobacion(a),True)

    def test_productoTensor(self):
        a=[[(3,2),(5,-1),(0,2)],[(0,0),(12,0),(6,-3)],[(2,0),(4,4),(9,3)]]
        b=[[(1,0),(3,4),(5,-7)],[(10,2),(6,0),(2,5)],[(0,0),(1,0),(2,9)]]
        res=[[(3, 2), (1, 18), (29, -11), (5, -1), (19, 17), (18, -40), (0, 2), (-8, 6), (14, 10)], [(26, 26), (18, 12), (-4, 19), (52, 0), (30, -6), (15, 23), (-4, 20), (0, 12), (-10, 4)], [(0, 0), (3, 2), (-12, 31), (0, 0), (5, -1), (19, 43), (0, 0), (0, 2), (-18, 4)], [(0, 0), (0, 0), (0, 0), (12, 0), (36, 48), (60, -84), (6, -3), (30, 15), (9, -57)], [(0, 0), (0, 0), (0, 0), (120, 24), (72, 0), (24, 60), (66, -18), (36, -18), (27, 24)], [(0, 0), (0, 0), (0, 0), (0, 0), (12, 0), (24, 108), (0, 0), (6, -3), (39, 48)], [(2, 0), (6, 8), (10, -14), (4, 4), (-4, 28), (48, -8), (9, 3), (15, 45), (66, -48)], [(20, 4), (12, 0), (4, 10), (32, 48), (24, 24), (-12, 28), (84, 48), (54, 18), (3, 51)], [(0, 0), (2, 0), (4, 18), (0, 0), (4, 4), (-28, 44), (0, 0), (9, 3), (-9, 87)]]
        self.assertEqual(Complejos.productoTensor(a,b),res)
        
        
if __name__ == "__main__":
        unittest.main()
