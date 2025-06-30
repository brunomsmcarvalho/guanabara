#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas, o nome com tdass minusculas
#qtaS letras ao ttodo (sem considerar os espacos) e qntas letras term o primeiro nome
nome = str(input('Introduza o seu nome completo: ')).strip() #o strip elimina os espacos desnecvessarios a frente e atras caso sejam inseridos
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))