#faca um programa que leia o sexo de uma pessoa mas so aceita 'm' ou 'f'.
#cvaso esteja errado, peca a digitacao novamente at`e ter um valor correto
sexo = str(input('Digite seu sexo: [M/F] ')).upper()[0].strip()
while sexo not in 'M F': #loop que repete caso seja introduzido valores que n sejam M ou F
        sexo = str(input('ERRO, valor introduzido nao valido, introduza o seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print('Sexo {} registado com sucesso'.format(sexo))