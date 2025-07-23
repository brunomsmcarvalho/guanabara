#faca um programa que mostre na tela uma contagem regressivapara o estouro
#de fogos de artificios de 10 ate 0 com uma pausa de 1 seg entre eles
from time import sleep
for c in range (10,-1,-1):
    sleep(1)
    print(c)
sleep(1)
print('BUUUUUMMMMM!!! HAPPY NEW YEAR')

