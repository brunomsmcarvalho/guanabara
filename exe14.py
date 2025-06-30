# escreva um programa que converta uma temperatura digitada em C e converta para F.
t=float(input('Apresente a temperatura em ºC: '))
c = (9*t)/5+32
print('A temperatura de {}ºC corresponde a {}ºF'.format(t,c))