#faca um programa que leia o peso de cinco pessoas , mostre qual foi
#o maior e o menor peso lidos
pesos = []
for i in range(1,6):
    peso = float(input('Peso da {}ª pessoa:  '.format(i)))
    pesos.append(peso)
peso_max = max(pesos)
peso_min = min(pesos)
print('A pessoa com maior peso tem {} e a pessoa com menos peso tem {}'.format(peso_max,peso_min))

'''
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}a pessoa'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
         maior = peso
        if peso < menor:
         menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
'''