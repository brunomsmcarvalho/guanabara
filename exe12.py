#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Insira o valor da sua compra para atribuição de desconto: '))
d = p - (p*.05)
print('Obteve .5%. de desconto a sua conta final é: {:.2f} R$'.format(d))