#refaca o desafio 35 dos triangulos acrescentando o recurso de mostrar
#que tipo de triangulo sera formado. Equilatero:todos os lados iguais.
#isosceles dois lados iguais. escaleno todos os lados diferentes
print('.=.'*10)
print('   Analisador de triângulos')
print('.=.'*10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os 3 segmentos acima CONSEGUEM FORMAR um triangulo ', end='')#o fim da linha n vai ser nd, nao vai ter o enter no fim da linha, aglomerando os prints a baixo
    if r1 == r2 and r1 == r3:#condicoes aninhadas
        print('EQUILATERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISOSCELES')
    else:#nao preciso voltar a verificar, se nao for o 1 ou 2 entao `e algo diferente
    #elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO')
else:
    print('Os 3 segmentos NÃO FORMAM um triangulo')