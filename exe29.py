#escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80kmh mostre uma mensagem a dizer que foi multaDO
#A muilta vai custar 7$ por cada km acima do limite
velocidade = float(input('A que velocidade está o seu carro: '))
multa = (velocidade-80)*7
if velocidade > 80:
    print('-=-'*20)
    print('Tenha atenção à velocidade, foi multado a cima do limite de 80km/h!!\n                  Tem a pagar {}€'.format(multa))
    print('-=-'*20)
else:
    print('Continue a ser um bom cidadão. Está dentro dos lities de velocidade')