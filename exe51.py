#desenvolva um programa que leia o primeiro termo e a razao de uma PA. no
#final mostre os 10 primeiros termos dessa progressa. PA progressao aritimetica
x = int(input('Digite o numero inicial da progressao aritmetica: '))
y = int(input('Razao: '))
decimo = x + (10-1) * y#de forma matematica dizemos que este `e o nosso decimo valor
for c in range(x,decimo+y,y):#vai contar de x ate decimo saltando de y em y

    print('{}'.format(c),end='->')#o end faz com que os valores sejam apresentados na mesma linha
print('ACABOU')