#melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10
#so que agora o jogador vai tentar adivinhar at`e acertar, mostrando no final
#quantos palpites foram necessarios para vencer
from random import randint
from time import sleep #importa da tabela time a funcao sleep que faz esperar por (x) segundos
x = randint(1,10)
tentativas = 0
acertou = False
print('-=-' * 20)  # multiplica uma sequencia de caracteres por 20 *
print('Estou a pensar num numero entre 0 e 10. Tenta adivinhar...')
print('-=-' * 20)
while not acertou:
    print('Em que numero eu pensei?')
    jogador = int(input('Numero: '))
    print('A PROCESSAR...')
    sleep(1)  # faz uma pausa no programa de (x) segundos a espera para criar suspanse
    tentativas += 1
    if jogador == x:
        acertou = True
    else:
        if jogador < x:
            print('Valor muito baixo...Tente outra vez')
        elif jogador > x:
            print('Valor muito alto...Tente outra vez')
print('=-=' * 14)
print('ACERTOU, utilizou {} tentativas PARABENS!!!'.format(tentativas))
print('=-=' * 14)
