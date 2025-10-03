'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre: a- Qntas vezes apareceu
o valor 9. b- em que posição foi digitado o primeiro valor 3
c-quais foram ops números pares
'''
tupla = ()
pares = ()
for i in range(0, 4):
    valor = int(input('Digite um valor: '))
    tupla += (valor,)
    if valor % 2 == 0:
        pares += (valor,)
print(f'Os números digitados foram: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 aparece primeiro na {tupla.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares digitados foram {pares}')


