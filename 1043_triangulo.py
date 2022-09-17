#1043_triangulo
a,b,c = (input().split())
A = float(a)
B = float(b)
C = float(c)

if (A+B)>C and (A+C)>B and (B+C)>A:
    perimeter = (A+B+C)
    print(f"Perimetro = {perimeter:0.1f}")
else:
    area = 0.5*(A+B)*C
    print(f"Area = {area:0.1f}")