#faca um programa que leia um numero inteiro e diga se ele `e ou nao um numero primo
num = int(input('Introduza um número, o programa vai verificar se ele é primo: '))
tot = 0
for i in range (1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('E por isso ele `e PRIMO')
else:
    print('E por isso ele NAO `e primo')