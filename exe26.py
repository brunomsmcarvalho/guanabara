#Faca um programa que lei uma frasre pelo teclado e mostrte: qntas vezes aparece a letrta 'a'. em q posicao ela aparece pela primeira vez. e em que posicao ela aparece na ultima vez
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima letra "A" aparece na posicao {}'.format(frase.rfind('A')+1))