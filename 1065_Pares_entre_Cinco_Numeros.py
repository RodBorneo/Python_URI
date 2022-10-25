#1065_Pares_entre_Cinco_Numeros
contador = 0

for i in range(5):
    nums = int(input())
    if(nums%2 == 0):
       contador+=1
print(f'{contador} valores pares')