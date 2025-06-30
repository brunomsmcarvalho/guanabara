#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantosa dólares ela pode comprar
#concidere US$ 1.00 = R$3.27
v1=float(input('Quanto dinheiro tem na sua carteira? Vamos converter para dólares:R$ '))
d=v1/5.54
E=v1/6.41
print('Com {:.2f}R$ consegue comprar:\n{:.2f}$ dólares!\nE \n{:.2f}€ Euros!'.format(v1,d,E))