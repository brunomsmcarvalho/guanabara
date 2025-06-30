#crie um programa q leia um número real qlqr pelo teclado e mostre na tela a sua porção inteira
#ex digite 6.127, parte inteira 6 (modulo math)
'''from math import trunc
v1 = float(input('Digite um valor: '))
print(('O numero digitado foi {}, a sua parte inteira do número é {} ').format(v1, trunc(v1)))'''
v1 = float(input('Digite um valor: '))
print(('O número digitado foi, {} e a sua parte inteira é: {}').format(v1, int(v1)))