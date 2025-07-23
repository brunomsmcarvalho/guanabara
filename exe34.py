#escrevas um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1250$ calcule um aumento de 10%
#para os inferiores ou iguais o aumento e de 15%
salario = float(input('Qual é o seu salário? Em €: '))
if salario > 1250:
    novo_salario = salario * 1.10
elif salario <= 1250:
    novo_salario = salario * 1.15
print('O seu salário passou de {:.2f}€ para {:.2f}€'.format(salario,novo_salario))