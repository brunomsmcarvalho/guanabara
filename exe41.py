#a confed nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idd: ate 9anos Mirim.ate 14 infantil
#ate 19 anos junior.ate 20 anos senior. acima mastrer
from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
classificacao = atual - nascimento
if classificacao <= 9:
    print('Este atleta com {} anos pertence aos MIRINS.'.format(classificacao))
elif classificacao <= 14:
    print('Este atleta com {} anos pertence aos INFANTIlS.'.format(classificacao))
elif classificacao <= 19:
    print('Este atleta com {} anos pertence aos JUNIORS.'.format(classificacao))
elif classificacao <= 20:
    print('Este atleta com {} anos pertence aos SENIORS.'.format(classificacao))
else:
    print('Este atleta com {} anos pertence aos MASTERS.'.format(classificacao))