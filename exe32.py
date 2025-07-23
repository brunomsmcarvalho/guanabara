#faca um programa que leia um ano qlqr e mostrte se ele 'e bissexto
from datetime import date
while True:
    ano = int(input('Introduza um ano para verificar se ele é bissexto: \nOu escreva "0" para ver o ano atual!!'))
    if ano == 0:
        ano = date.today().year
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:

        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')