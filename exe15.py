'''
Escreva um programa que pergunte a qntdd de km percorridos por um carro
alugado e a qntdd de dias pelos quais ele foi alugado. calcule o preço a
pagar, sabendo que o carro ccusta R$60 por dia e R$0,15 por km rodado
'''
d=int(input('Por qauntos dias alugou o carro? '))
km=float(input('Qauntos Km andou com o carro? '))
print('Você alugou o carro por {} dias, custa {:.2f}R$ \nPercorreu {}Km, custa {:.2f}R$'.format(d,(d*60),km,(km*0.15)))
print('A sua conta final são {:.2f}R$'.format((d*60)+(km*0.15)))