#1060_numeros_positivos
contador = 0

for i in range(6):
    nums = float(input())
    if(nums>0):
       contador+=1
print(f'{contador} valores positivos')