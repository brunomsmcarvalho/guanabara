#faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor
a = int(input('Indique o primeiro valor: '))
b = int(input('Indique o segundo valor: '))
c = int(input('Indique o terceiro valor: '))
#verifica o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verifica o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))