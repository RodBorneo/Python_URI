#1021 - Notas e Moedas

valor = float(input())
valor += 0.001 #essa linha é necessária devido ao problema de arredondamento
#esse problema é comum em muitas linguagens


if (valor > 0) and (valor < 1000000.00):
  notas_100 = int(valor/100)
  resto_100 = float(valor%100)

  notas_50 = int(resto_100/50)
  resto_50 = float(resto_100%50)

  notas_20 = int(resto_50/20)
  resto_20 = float(resto_50%20)

  notas_10 = int(resto_20/10)
  resto_10 = float(resto_20%10)

  notas_5 = int(resto_10/5)
  resto_5 = float(resto_10%5)

  notas_2 = int(resto_5/2)
  resto_2 = float(resto_5%2)


  moedas_1 = int(resto_2/1)
  rest_moedas_1 = float(resto_2%1)

  moedas_050 = int(rest_moedas_1/0.50)
  rest_moedas_050 = float (rest_moedas_1%0.50)

  moedas_025 = int(rest_moedas_050/0.25)
  rest_moedas_025 = float (rest_moedas_050%0.25)

  moedas_010 = int(rest_moedas_025/0.1)
  rest_moedas_010 = float(rest_moedas_025%0.1)

  moedas_005 = int(rest_moedas_010/0.05)
  rest_moedas_005 = float(rest_moedas_010%0.05)

  moedas_001 = int(rest_moedas_005/0.01)

  print("NOTAS:")
  print(notas_100, "nota(s) de R$ 100.00")
  print(notas_50, "nota(s) de R$ 50.00")
  print(notas_20, "nota(s) de R$ 20.00")
  print(notas_10, "nota(s) de R$ 10.00")
  print(notas_5, "nota(s) de R$ 5.00")
  print(notas_2, "nota(s) de R$ 2.00")

  print("MOEDAS:")
  print(moedas_1, "moeda(s) de R$ 1.00")
  print(moedas_050, "moeda(s) de R$ 0.50")
  print(moedas_025, "moeda(s) de R$ 0.25")
  print(moedas_010, "moeda(s) de R$ 0.10")
  print(moedas_005, "moeda(s) de R$ 0.05")
  print(moedas_001, "moeda(s) de R$ 0.01")
