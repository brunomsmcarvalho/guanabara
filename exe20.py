#o mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. faç um programa que leia
# o nome dos 4 alunos e mostre a ordem sorteada
'''import random
nome = ['João','Maria','Paula','António']
v = random.shuffle(nome)
print (f'O primeiro a apresentar é 0(a) {nome[0]}\nO segundo a apresentar é o(a) {nome[1]}\nO terceiro a apresentar é o(a) {nome[2]}\nO quarto a apresentar é o(a) {nome[3]} ')'''
from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
nome = [n1,n2,n3,n4]
v = shuffle(nome)
print (f'O primeiro a apresentar é 0(a) {nome[0]}\nO segundo a apresentar é o(a) {nome[1]}\nO terceiro a apresentar é o(a) {nome[2]}\nO quarto a apresentar é o(a) {nome[3]} ')
