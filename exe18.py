#faça um programa que leia um angulo qlqr e mostre na tela o valor do seno cosseno e tangente desse angulo
import math
ang=float(input('Digite o valor do angulo: '))
cosseno=math.cos(math.radians(ang))
print('O Cosseno de {:.0f} é {:.2f}'.format(ang, cosseno))
seno=math.sin(math.radians(ang))
print('O Seno de {:.0f} é {:.2f}'.format(ang, seno))
tangente = math.tan(math.radians(ang))
print('A Tangente de {:.0f} é {:.2f}'.format(ang, tangente))