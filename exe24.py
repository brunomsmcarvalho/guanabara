#crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "santo"
cidade = str(input('Introduza a cidade onde voce nasceu: ').strip())
print(cidade[:5].upper() == 'SANTO')

