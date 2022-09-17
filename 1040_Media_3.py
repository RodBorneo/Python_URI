#1040 - Media 3

n1,n2,n3,n4 = input().split(" ")

N1 = float(n1)
#N1 = round(N1,1)

N2 = float(n2)
#N2 = round(N2,1)

N3 = float(n3)
#N3 = round(N3,1)

N4 = float(n4)
#N4 = round(N4,1)

P1 = N1 * 2
P2 = N2 * 3
P3 = N3 * 4
P4 = N4 * 1

Media = (P1+P2+P3+P4)/(2+3+4+1)
#Media = round(Media,1)


if(Media >= 5.0 and Media <=6.9):
  N_exame = float(input())
  print('Media: {:.1f}'.format(Media))
  Nova_media = (Media + N_exame)/2
  print("Aluno em exame.")
elif (Media >= 7.0):
  print('Media: {:.1f}'.format(Media))
  print("Aluno aprovado.")
else:
  print('Media: {:.1f}'.format(Media))
  print("Aluno reprovado.")  


if(Media >= 5.0 and Media <=6.9):
  print('Nota do exame: {:.1f}'.format(N_exame))
  Nova_media = (Media + N_exame)/2

  if (Nova_media >= 5.0):
    print("Aluno aprovado.") 
    #print("Media final:", Nova_media)
    print('Media final: {:.1f}'.format(Nova_media)) 
  else:
      print("Aluno reprovado")
      #print("Media final:", Nova_media)
      print('Media final: {:.1f}'.format(Nova_media))
