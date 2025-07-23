#escreva um programa que leia um numero inteiro qlqr e peca para o usuario
#qual sera a base de conversao 1 para binario 2 para octal 3 para hexadecimal
x = int(input('Digite um numero inteiro: '))
print('''[ 1 ] - Converter para BINARIO
[ 2 ] - Converter para OCTAL
[ 3 ] - Converter para HEXADECIMAL''')
a = int(input('Opcao: '))
#a = int(input('Vamos converter o numero inteiro:\n[ 1 ]Para converter para binario\n[ 2 ]Para converter em Octal\n[ 3 ]Para conmverter em Hexadecimal\nOpcao: '))

if a == 1 :
    print('O numero {} convertido para BINARIO `e: {}'.format(x, bin(x)[2:]))#o python tem de forma nativa a conversao para estas linguagens
elif a == 2 :
    print('O numero {} convertido para OCTAL `e: {}'.format(x,oct(x)[2:]))#na resposta aparece um codigo que nao fica mt interessante para o usuario
elif a == 3 :
    print('O numero {} convertido para HEXADECIMAL `e: {}'.format(x,hex(x)[2:]))#com o codigo[2:] fazemos com quie a resposta comece no 3 caracter e va ate o final
else:
    print('Valor introduzido incorrecto!!')