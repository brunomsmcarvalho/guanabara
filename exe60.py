# faca um programa que leia um numero qlqr e mostre o seu factorial
#Ex.: 5! = 5x4x3x2x1 = 120 , a seguir fazer com o while tentar com o for
'''
num = int(input('Introduza um numero `a escolha para calcular o seu fatorial: '))
num2 = 1
while num2 >= 1:
    num2=num2*num
    num1=num1-1 
    print (v2)'''
'''soma = 1
for c in range(1,num+1):
    soma *= c
print(soma)'''
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-= 1
print('O factorial de {} `e {}'.format(n,f))