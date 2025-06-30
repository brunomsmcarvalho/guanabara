#escreva um programa que faca o computador pensar em um numero inteiro entre 0 e 5 e peca para o usuario tentar
#descobrir qual foi o numero escolhido pelo computador. O programa deve escrever na tela se o usuario ganhou ou perdeu
from random import randint
from time import sleep #importa da tabela time a funcao sleep que faz esperar por (x) segundos
while True:
    x = randint(1,5)
    print('-=-'*20) #multiplica uma sequencia de caracteres por 20 *
    print('Esrtou a pensar num numero entre 0 e 5. Tenta adivinhar...')
    print('-=-'*20)
    jogador = int(input('Em que numero eu pensei?'))
    print('PROCESSANDO...')
    sleep(2) #faz uma pausa no programa de (x) segundos a espera para criar suspanse
    if jogador != x:
        print('=-=' * 20)
        print('Errou! Eu pensei no numero {} e nao no {}'.format(x,jogador))
        print('=-=' * 20)
    else:
        print('Parabens, voce acertou no numero!!')
        break