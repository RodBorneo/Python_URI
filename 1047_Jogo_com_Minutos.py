#1047 Tempo de jogo com minutos
h_in, min_in, h_fim, min_fim = (input().split())

a = int(h_in)
c = int(min_in)
b = int(h_fim)
d = int(min_fim)

#converte o horario para o total em minutos
h_final = (b*60) + d
#print(h_final)

h_inicial = (a*60)+c
#print(h_inicial)

dif = h_final - h_inicial

#soma 1 dia caso a dif seja <=0
if(dif<=0):
    dif+=24*60
    
hora = dif//60
minuto = dif%60
print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")