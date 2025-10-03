'''
Crie um programa onde o usuario possa digitar cinco valoresnuméricos
e cadastre-os numa lista, já na posição correta de inserção (sem usar o .sort).
no final mostre a lista ordenada na tela.
'''
lista = list()
min = 0
max = 0
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores adiconados em ordem são {lista}')