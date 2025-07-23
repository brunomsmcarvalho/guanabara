#crie um programa que leia uma frase qualquer e diga se ela `e um palindromo
#desconsiderando os espacos. EX: 'APOS SOPA''A SACADA DA CASA''A TORRE DA DERROTA'
#da para ler de tras para a frente e de frentge para tras
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()#separa a frase e cria uma lista
junto = ''.join(palavras)#junta a lista para eliminar os espacos
#inverso = '' \ podemos fazer sem o for desta forma
inverso = junto[::-1]
#for letra in range(len(junto)-1,-1,-1):#vai da ultima letra(len(junto)-1 ate a primeira -1 de tras para a frente
    #inverso += junto[letra]#cria a frase de forma invertida
print('O inverso de {} `e {}'.format(junto, inverso))
if inverso == junto:#verifica se a frase `e igual de frnt p tras e tras p frnt
    print('Temos um palindromo')
else:
    print('A frase digitada nao `e um palindromo!')
