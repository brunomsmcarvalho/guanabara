#escreva um prograsma que leia dois numeros inteiros e compare.os, mostrando na tela
#uma mensagem: o primeiro valor 'e maior, o segundo valor 'e maior nao existe valor maior, os dois sao iguais
num1 = int(input('Digite o primeito numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    print('O numero {} `e maior que o numero {}'.format(num1,num2))
elif num1 < num2:
    print('O numero {} `e maior que o numero {}'.format(num2,num1))
else:
    print('Nao existe numero maior, ambos sao iguais.')
