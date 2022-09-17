#1041_Coordenadas_de_ponto

#x,y = list(map(float,input().split()))
eixo_X,eixo_Y = (input().split())
x = float(eixo_X)
y = float(eixo_Y)
if(x==0 and y==0):
    print("Origem")
elif(x==0):
    print("Eixo Y")
elif(y==0):
    print("Eixo X")
elif(x>0 and y>0):
    print("Q1")
elif(x<0 and y>0):
    print("Q2")
elif(x<0 and y<0):
    print("Q3")
elif(x>0 and y<0):
    print("Q4")