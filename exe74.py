'''
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior que estão na tupla
'''
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
#print(f'Os 5 valores sorteados são: {n}')
print('Os valores sorteados foram:', end=' ')
for n in num:
    print(f'{n} ', end=' ')
print(f'\nO maior valor sorteado foi: {max(num)}')
print(f'O menor valor sorteado foi: {min(num)}')
