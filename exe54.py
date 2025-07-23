#crie um programa que leia o ano de nascimento de sete pessoas. No final,
#mostre quantas pessoas ainda nao atingiram a maioridade e qnts ja sao maiores
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(0,7):
    idades = int(input('Em que ano a {}ª pessoa nasceu? '.format(i+1)))
    idades = atual - idades #calcula quantos anos a pessoa tem
    if idades >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idades'.format(totmaior))
print('E o total de {} pessoas menores de idades'.format(totmenor))
