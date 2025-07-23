#refaca o desafio 009, mostrando a tabuada de um numero que o ususario
#escolher so que agora utilizando um laco for
'''v1=int(input('Introduz um número à tua escolha para ver a tabuada: '))
print('A tabuada de {} é :'.format(v1))
print('_' * 12)
print('1 x {:2} = {}'.format(v1,v1*1))
print('2 x {:2} = {}'.format(v1,v1*2))
print('3 x {:2} = {}'.format(v1,v1*3))
print('4 x {:2} = {}'.format(v1,v1*4))
print('5 x {:2} = {}'.format(v1,v1*5))
print('6 x {:2} = {}'.format(v1,v1*6))
print('7 x {:2} = {}'.format(v1,v1*7))
print('8 x {:2} = {}'.format(v1,v1*8))
print('9 x {:2} = {}'.format(v1,v1*9))
print('10 x {} = {}'.format(v1,v1*10))
print('_' * 12)'''
v1 = int(input('Indique o valor para tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(v1,c,v1*c))#:2 vai mexer na posicao do c para ficar mais harmonioso