'''
crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso de 0 a 20. Seu programa deverá ler um número
pelo teclado entre 0 a 20 e mostrar-lo por extenso
'''
from time import sleep
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    while True:
        num = int(input('Escolha um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente! ',end='')
    print(f'Você digitou o número {extenso[num]}')
    continuar = input('Deseja continuar? S/N').strip().upper()[0]
    if continuar == 'N':
        print('Encerrando o programa...')
        sleep(1)
        print('...')
        sleep(1)
        print('..')
        sleep(0.8)
        print('.')
        sleep(0.6)
        print('Adeus!!')
        break

