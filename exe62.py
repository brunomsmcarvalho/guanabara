#melhore o desafio 61 perguntando para o usuario se ele quer mostrar mais
#alguns termos. O programa encerra qnd ele disser que quer mostrar 0 termos
print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Digite o numero inicial da progressao aritmetica: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1 #cont = contador
mais = 10
total = 0
while mais != 0:
    total = total + mais
    print('{}'.format(cont), end='->')
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Digite quantos numeros mais quer mostrar: \n0 Para terminar'))
print('Progressao finalizada com {} termos mostrados'.format(total))
