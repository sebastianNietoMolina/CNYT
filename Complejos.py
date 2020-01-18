import math

def imprimir(ente,imag):
    if imag<0:
        res=str(ente)+str(imag)+'i'
    elif imag==0:
        res=str(ente)
    else:
        res=str(ente)+'+'+str(imag)+'i'
    return res

def sumar(a,b):
    ente=a[0]+b[0]
    imag=a[1]+b[1]
    return (ente,imag)    

def restar(a,b):
    ente=a[0]-b[0]
    imag=a[1]-b[1]
    return (ente,imag)    

def multiplicar(a,b):
    ente=a[0]*b[0]+(b[1]*a[1])*-1
    imag=a[0]*b[1]+a[1]*b[0]
    return (ente,imag)    

def modulo(a):
    return (math.sqrt((a[0]**2+a[1]**2)))
    
def division(a,b):
    div=b[0]**2+b[1]**2
    ente=(a[0]*b[0]+a[1]*b[1])/div
    imag=(a[1]*b[0]-a[0]*b[1])/div
    return (ente,imag)    

def conjugado(a):
    ente=a[0]
    imag=a[1]*-1
    return (ente,imag)

def cartesianoPolar(a,b):
    p=(math.sqrt(a**2+b**2))
    o=(math.atan(b/a))
    return (p,o)
    
        
        
