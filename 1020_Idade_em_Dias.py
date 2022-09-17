#1020 - Idade em Dias

idade_em_dias = int(input())

ano = int(idade_em_dias/365)
meses = int((idade_em_dias % 365) / 30)
dias = int(idade_em_dias % 365 % 30)

print(ano, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")