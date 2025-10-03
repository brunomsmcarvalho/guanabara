'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro ,
ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não adicionado..')
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Os números digitados foram: {lista}')
lista.sort()
print(f'Os números ordenados de forma crescente são {lista}')

