'''faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
ex:1834 aparecer unidade deszena centena milhar fazer em str e matematicamente'''
import random
numero = random.randint(0,9999)
print('O seu numero é: {}'.format(numero))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('O seu numero tem: \n{} nas unidadses\n{} nas dezenas\n{} nas centenas\n{} nos milhares'.format(u,d,c,m))