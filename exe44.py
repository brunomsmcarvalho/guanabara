#elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preco normal e condicao de pagamento:
#a vista dinheiro cheque 10%desc.a vista no cartao 5%desconto. em ate 2xno cartao preco normal
#3xoumais no cartao 20%de juros
print('{:=^40}'.format(' LOJAS CARVALHO ')) #este codigo vai centralizar ^ a mensagem em 40 espacos
preco = float(input('Indique o valor do produrto: '))
print('''Escolha a opcao de pagamento
[ 1 ] A vista com dinheiro ou cheque
[ 2 ] A vista com cartao
[ 3 ] 2 X no cartao
[ 4 ] 3 X ou mais no cartao''')
a = int(input('Opcao: '))
if a == 1:
    precoinc = preco - preco * 0.1
elif a == 2:
    precoinc = preco - preco * 0.05
elif a ==3:
    precoinc = preco
    parcela = preco / 2
    print('Sua compra vai ser parcelada em 2x de {:.2f}R$ SEM JUROS'.format(parcela))
elif a == 4:
    parcela = int(input('Quantas parcelas? '))
    precoinc = preco * 1.2
    parcelas = preco / parcela
    print('Sua compra sera parcelada em {}X de R$ {:.2f} COM JUROS'.format(parcela,parcelas))
else:
    print('Valor introduzido invalido')
print('De {}$ vc tem a pagar {}$'.format(preco , precoinc))
