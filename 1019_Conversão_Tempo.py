#1019 - Conversão de Tempo

tempo = int(input())
hours = int(tempo / 3600)
minutes = int((tempo % 3600) / 60)
seconds =  (tempo % 3600 % 60)

print("{}:{}:{}".format(hours, minutes, seconds))