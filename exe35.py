#desenvolva um programa que leia o cumprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
print('.=.'*10)
print('   Analisador de triângulos')
print('.=.'*10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os 3 segmentos acima CONSEGUEM FORMAR um triangulo')
else:
    print('Os 3 segmentos NÃO FORMAM um triangulo')
