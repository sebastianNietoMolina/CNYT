import Complejos as c

def sistemaCuanticoParticulaEnUnaLinea(vec,pos):
    res=0
    k=vec[pos]
    res2=k[0]*k[0]+k[1]*k[1]
    for c in vec:
        res+=c[0]*c[0]+c[1]*c[1]
    p=res2/res
    return p

def valorEsperado(fi,si):
    multUno=c.productoMatrizVector(fi,si)
    multDos=c.productoInternoVectores(multUno,si)
    return multDos
    
    
