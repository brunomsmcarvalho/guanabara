'''faca um programa que leia o nome completoi de uma pessoa, mostrando em seguida o priemeiro e o ultimo nome separados.
ex: Ana Maria de Souza primeiro ana ultimo souza. acontecer para qlqr tamanho de str'''
nome = str(input('Digite o seu nome completo: ')).strip().capitalize()
print('Muito prazer em te conhecer')
print('O seu primeiro nome e {}'.format(nome.split()[0]))
print('O seu ultimo nome e {}'.format(nome.split()[-1].capitalize()))
