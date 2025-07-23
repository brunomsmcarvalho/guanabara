#faca um programa que leia o ano de nascvimento de um jovem e informe de acordo com a sua idade
#se ele ainda vai se alistar ao servico militar, se 'e hora de se alistar,se ja passou do tempo do alistamento
#seu programa tb devera mostrar o tempo que falta ou qye passou do prazo
from datetime import date
nascimento = int(input('Indique o ano em que nasceu: '))
atual = date.today().year
idd = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idd, atual))

if idd == 18:
    print('Esta na hora de se alistar!!')

elif idd > 18:
    idd_superior = idd - 18
    print('Ja passou o tempo de se alistar em {} anos!!'.format(idd_superior))
    ano = atual - idd_superior
    print('Seu alsitamento foi em {}'.format(ano))

else:
    idd_inferior = 18 - idd
    print('Ainda nao esta na hora de se alistar, faltam {} anos!!'.format(idd_inferior))
    ano = atual + idd_inferior
    print('Seu alistamento ser`a em {}'.format(ano))
