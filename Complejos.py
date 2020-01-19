import math

def sumar(a,b):
    """Resuelve la suma de 2 numeros complejos.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.
    b -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    ente=a[0]+b[0]
    imag=a[1]+b[1]
    return (ente,imag)    

def restar(a,b):
    """Resuelve la resta de 2 numeros complejos.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.
    b -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    ente=a[0]-b[0]
    imag=a[1]-b[1]
    return (ente,imag)    

def multiplicar(a,b):
    """Resuelve la multiplicacion de 2 numeros complejos.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.
    b -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    ente=a[0]*b[0]+(b[1]*a[1])*-1
    imag=a[0]*b[1]+a[1]*b[0]
    return (ente,imag)    

def modulo(a):
    """Resuelve el modulo de un numero complejo.

    Devuelve una tupla de un real.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    return (math.sqrt((a[0]**2+a[1]**2)))
    
def division(a,b):
    """Resuelve la division de 2 numeros complejos.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.
    b -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    div=b[0]**2+b[1]**2
    ente=(a[0]*b[0]+a[1]*b[1])/div
    imag=(a[1]*b[0]-a[0]*b[1])/div
    return (ente,imag)    

def conjugado(a):
    """Resuelve el conugado de un numero complejo.

    Devuelve una tupla con la parte real y la parte imaginaria.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    ente=a[0]
    imag=a[1]*-1
    return (ente,imag)

def cartesianoPolar(a):
    """Cambia de coordenadas cartesianas a polares de un numero complejo.

    Devuelve una tupla con la parte real y un angulo.

    Parametros:
    a -- Es una tupla que contiene parte real y la parte imaginaria del numero complejo.

    """
    p=(math.sqrt(a[0]**2+a[1]**2))
    o=(math.atan(a[1]/a[0]))
    return (p,o)

def polarCartesiano(p):
    """Cambia de coordenadas polares a cartesianas de un numero complejo.

    Devuelve una tupla con la parte real y la parte imaginaria del numero complejo.

    Parametros:
    p -- Es una tupla que contiene parte real y un angulo.

    """
    a=round(p[0]*math.cos(p[1]),3)
    b=round(p[0]*math.sin(p[1]),3)
    return (a,b)
        
        
