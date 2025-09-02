#refaca o exe 51 lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da
#progressao usando estyrutura while
'''decimo = x + (10-1) * y#de forma matematica dizemos que este `e o nosso decimo valor
for c in range(x,decimo+y,y):#vai contar de x ate decimo saltando de y em y

    print('{}'.format(c),end='->')#o end faz com que os valores sejam apresentados na mesma linha
print('ACABOU')'''
from exe48 import cont

print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Digite o numero inicial da progressao aritmetica: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1 #cont = contador
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')