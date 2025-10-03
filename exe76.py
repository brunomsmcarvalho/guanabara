'''
crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em
forma tabular
'''
produtos = (
    'Caderno',2.45,
    'Caneta',3.00,
    'Borracha',0.65,
    'Afia',1.20,
    'Agenda',6.00,
    'Estojo',15.00,
    'Mochila',76.00
)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end=' ')
    else:
        print(f'R${produtos[item]:>7.2f}')
