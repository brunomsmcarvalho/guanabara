#crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final de acordo com a media atingida
#media abaixo de 5 reprovado.media entre 5 e 6.9 recuperacao. media 7 ou superior aprovado
nota1 = float(input('Indique a sua primeira nota: '))
nota2 = float(input('Indique a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno `e {:.1f}'.format(nota1,nota2,media))
if media < 5.0:
    print('\033[31mREPROVADO!\033[m')
elif media >= 5.0 and media <= 6.9:
    print('\033[33mRECUPERACAO!\033[m')
else:
    print('\033[32mAPROVADO!\033[m')

