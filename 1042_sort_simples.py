#1042_sort_simples

x,y,z = (input().split())
n1 = int(x)
n2 = int(y)
n3 = int(z)
list = [n1,n2,n3]
ord = sorted(list)


print(f"{ord[0]}\n{ord[1]}\n{ord[2]}")
print(f"\n{n1}\n{n2}\n{n3}")