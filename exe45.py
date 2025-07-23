from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[7;34;40m  SUAS OPÇÕES  \033[m
\033[7;34;40m[ 0 ] PEDRA    \033[m
\033[7;34;40m[ 1 ] PAPEL    \033[m
\033[7;34;40m[ 2 ] TESOURA  \033[m''')
jogador = int(input('\033[7;37;40mQual `e a sua jogada: \033[m'))
print('\033[35mJO\033[m')
sleep(1)
print('\033[31mKEN\033[m')
sleep(1)
print('\033[32mPO!!!\033[m')
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0:#computador jogou PEDRA
    if jogador == 0:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    else:
        print('\033[31mJOGADA INVALIDA\033[m')
elif computador == 1:#computador jogou PAPEL
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    else:
        print('\033JOGADA INVALIDA\033[m')
elif computador == 2:#computador jogou TESOURA
    if jogador == 0:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATE\033[m')
    else:
        print('\033[31mJOGADA INVALIDA\033[m')