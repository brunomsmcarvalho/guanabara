#um professor quer sortear um dos seus quatro alunos para apagar o qaudro.
# Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido
'''import random
nome = [ 'João', 'Maria','Paula','António' ]
print(nome)
escolhido = random.choice(nome)

print(f'O aluno escolhido para apagar o quadro foi: {escolhido}')'''
from random import choice
a1 = str(input('Indique o primeiro aluno: '))
a2 = str(input('Indique o segundo aluno: '))
a3 = str(input('Indique o terceiro aluno: '))
a4 = str(input('Indique o quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido para apagar o quadro foi {}'.format(escolhido))

