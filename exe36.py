#escreva um programa para aprovar um emprestimo bancario para a compra de uma casa
#o prioigrama vai perguntar valor da casa, o salario do comprador e em qnts anos ele vai pagar
#calcule o valor da prestacao mensal sabendo que ela nao pode exceder 30% do salario
#ou entao o emprestimo sera neghado
print('_=_Vamos calcular o seu emprestimo bancario_=_')
a = float(input('Insira o valor da casa: '))
b = float(input('Insira o valor do seu salario: '))
c = int(input('indique em quantos anos ira pagar a casa: '))
prestacao_casa = (a / c) / 12
print('Para pagar uma casa de {:.2f}$ em {} anos, a prestacao sera de {:.2f}$'.format(a,c,prestacao_casa))
if prestacao_casa >= (0.3 * b):
    print('Emprestimo NEGADO')
else:
    print('Emprestimo APROVADO!!')