#1012 - AREA:

A, B, C = input().split(" ")

a = float(A)
b = float(B)
c = float(C)
pi = 3.14159

a_tri = (a*c)/2
print("TRIANGULO: %.3f" %a_tri)

a_circulo = pi*(c**2)
print("CIRCULO: %.3f" %a_circulo)

a_trapezio = ((a+b)*c)/2
print("TRAPEZIO: %.3f" %a_trapezio)

a_quadrado = (b**2)
print("QUADRADO: %.3f" %a_quadrado)

a_retangulo = (a*b)
print("RETANGULO: %.3f" %a_retangulo)
