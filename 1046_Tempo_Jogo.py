#1046_Tempo_Jogo
a,b = (input().split())
A = int(a)
B = int(b)

if(A<B):
    time=B-A
else:
    time=B+24-A
print(f"O JOGO DUROU {time} HORA(S)")