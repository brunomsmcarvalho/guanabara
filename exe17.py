#faça um program que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo rectangulo calcule e mostre o cmprimento da  hipotenusa
'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (co**2 + ca**2)**(1/2)
print('A hipotenusa é igual a {:.2f}'.format(h))'''
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h=math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(h))