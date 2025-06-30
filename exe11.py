#faça um programa que leia a largurta e a altura de uma parede em metros, cácule a sua área e as qntdd de tinta necessária para pintar.la, sabendo que cada litro de tinta pinta uma área de 2m^2
l=float(input('Indique a largura da sua parede: '))
a=float(input('Indique a altura da sua parede: '))
m2=l*a
t=m2/2
print('A área da sua parede é de {:.2f}m^2'.format(m2))
print('Para {:.2f}m^2 precisa de {:.2f} litros de tinta'.format(m2,t))