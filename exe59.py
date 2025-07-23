#crie um programa que leia dois valores e mostre um menu na tela:
#1somar 2 multiplicar 3 maior 4 novos numeros 5 sair do programa
#seu programa devera realizar a operacao solicitada em cada caso
from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
menu = 0
while menu != 5:
    print('''
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos numeros
[ 5 ] - Sair
    ''')
    menu = int(input('OPCAO: '))
    if menu == 1:
        v3 = v1 + v2
        print('{} + {} = {}'.format(v1, v2, v3))
    elif menu == 2:
        v3 = v1 * v2
        print('{} * {} = {}'.format(v1, v2, v3))
    elif menu == 3:
        if v1 > v2:
            print('{} `e maior que {}'.format(v1, v2))
        else:
            print('{} `e menor que {}'.format(v1, v2))
    elif menu == 4:
        print('Informe os valores novos.')
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
    elif menu == 5:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Opcao invalida. Tente novamente.')
print('Fim do programa. Volte sempre!')