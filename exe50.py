#desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas
#daqueles que forem pares. se o valor digitado for impar, desconsidera-o
soma = 0
for c in range(0,6):
    valores = int(input('Introduza 6 valores inteiros aleatorios: '))
    if valores % 2 == 0:
        soma += valores
print('A soma dos valores pares `e {}'.format(soma))