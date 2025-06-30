#crie um programa que leia um numero inteiro e mostrte na tela se ele e par ou impar
numero = int(input('Digite um numero inteiro: '))
if numero % 2 == 0:
    print('O numero {} é par!'.format(numero))
else:
    print('O numero {} é impar!'.format(numero))