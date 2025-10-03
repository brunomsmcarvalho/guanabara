'''
Faça um programa que leia 5 valores e guarde.os em uma lista
no final mostre qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista. se houver mais que um valor maior
mostrar todos os que são
'''
numeros = []
maior = 0
menor = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite um valor na posição {n}: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print('=.'*30)
print(f'Você digitou os valores {numeros}')
print('-'*60)
print(f'O maior valor digitado foi {maior} na posição', end=' ')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...',end='')
print(f'\nO menor valor digitado foi {menor} na posição',end=' ')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...',end='')
print()
print('=.'*30)
