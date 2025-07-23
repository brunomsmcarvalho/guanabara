#faca um programa que calcule a soma entre todos os numeros impares que sao
# multiplos de 3 e que se encontram no intervalo de 1 ate 500
soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0:
        cont += 1#um contador vai somar todos os valores que estao dentro das condicoes
        soma += c#um acomulador vai acumulando/multiplicando/dividindo os valores encontrados nas condicoes

print('A soma de todos os {} valores solicitados `e {}'.format(cont,soma))