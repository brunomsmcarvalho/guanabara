#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
v1 = float(input('Vamos converter em cm e mm o valor dos m introduzidos: '))
cm = v1*100
mm = v1*1000

print('{} metros correspondem a {} centímetros e {} milimetros'.format(v1,cm,mm))