'''
crie uma tupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol, na ordem de colocação. depois
mostre a-apenas os 5 primeiros colocados.b- os ultimos 4 colocados.
c-uma lista coms os times em orde alfabetica d-em que posição na
tabela está o time da chapecoense
'''
equipas25 = (
    'Flamengo','Palmeiras','Cruzeiro','Bahia','Botafogo','Mirassol','São Paulo','Fluminense','Bragantino','Ceará','Atlético-MG','Internacional','Grêmio','Corinthians','Santos','Vsc da Gama','Vitória','Juventude','Fortaleza','Recife'
)
print('=-'*150)
#for t in equipas25:
#    print(t) //  O print da tupla aparece uma posição uma por baixo da outra
print(f'As equipas do Brasileirão em 2025 --> {equipas25}')
print('=-'*40)
print(f'Os cinco primeiros colacados são: {equipas25[:5]}')
print('*-'*40)
print(f'Os últimos quatro colocados são {equipas25[-4:]}')
print('*-'*40)
print(f'As equipas por ordem alfabética: {sorted(equipas25)}')
print('-'*40)
print(f'O Botafogo está na {equipas25.index('Botafogo')+1}ª posição')
