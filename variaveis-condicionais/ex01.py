n1=int(input('Nota 1: '))
n2=int(input('Nota 2: '))
n3=int(input('Nota 3: '))
media=(n1+n2+n3)/3
print('A média das notas é {:.2f}'.format(media))
media_ponderada1=(n1*2+n2*2+n3*3)/7
print('A média ponderada das notas é {:.2f}'.format(media_ponderada1))
media_ponderada2=(n1*1+n2*2+n3*2)/5
print('A média ponderada das notas é {:.2f}'.format(media_ponderada2))