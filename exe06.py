#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
v=int(input('Escolha um número '))
print(' O dobro de {} vale: {:>10}\n O triplo vale: {:>14}\n E a raiz quadrada é: {:>11.2f}'.format(v,v*2,v*3,v**(1/2)))
#para fazer a raiz quadrada podemos tb usar a função power (pow) neste caso ficava pow(n,(1/2))