#desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC
#e mostre seu status, de acordo com a tabela abaixo:
#abaixo de 18.5:abaixo do peso. entre 18.5 e 25:peso ideal. de 25 a 30:sobrepesso.de 30 a 40:obesidade. acima de 40 obesidade morbida
altura = float(input('Indique a sua altura em M: '))
peso = float(input('Indique o seu peso em KG: '))
imc = peso / (altura ** 2)
print('O seu IMC - Indice de Massa Corporal `e {:.2f}'.format(imc))
if imc < 18.5:
    print('Vc est`a abaixo do peso indicado!')
elif imc >= 18.5 and imc < 25:
    print('Vc est`a no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Vc est`a com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Vc est`a com obesidade!')
else:
    print('Vc est`a com obesidade morbida!')
