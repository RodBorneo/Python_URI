#1013 - O Maior

A, B, C = input().split(" ")

a = int(A)
b = int(B)
c = int(C)

MaiorAB = int((a+b+abs(a-b))/2)

if MaiorAB > c:
  print("{} eh o maior".format(MaiorAB))
else:
  print("{} eh o maior".format(c))