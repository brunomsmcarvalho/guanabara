'''
crie um programa que tenha uma tupla com várias palabras não usar
acentos. depois disso, voce deve mostrar para cada palabra quais
são as suas vogais
'''
palavras = (
    'caderno',
    'contabilidade',
    'deputada',
    'escola',
    'futebol',
    'bola',
    'cuidado',
    'correr'
)
#cada plavra é uma listagem que podemos trabalhar individualmente usando um for dentro do outro
for palavra in palavras: #segue todas as palavras dentro da tupla individualmente
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra: #pega em cada palavra de forma de uma lista
        if letra.lower() in 'aeiou': #verifica em cada palavra se tem vogais
            print(letra, end=' ')