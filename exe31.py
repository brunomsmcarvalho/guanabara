#desenvolva um programa que pergunte a distancia de uma viagem em km. calcula o preco da passagem,
#cobrando 0.50$ por km poara viagens de ate 200km e 0.45$ para viagens mais longas
x = float(input('Digite a distancia percorrida em km: '))
if x > 201:
    y = x * 0.45
    print('O valor a cobrar da viagem é de {}R$'.format(y))
else:
    y = x * 0.5
    print('O valor a cobrar da viagem é de {:.2f}R$'.format(y))
#y = x * 0.5 if x <= 200 else x * 0.45
#isto 'e chamado o if simplificado