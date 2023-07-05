#Exercício Python 11: Faça um programa que leia a largura e a
# altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que
# cada litro de tinta pinta uma área de 2 metros quadrados.

a = float(input('Insira a altura: '))
l = float(input('Insira a largura: '))
area = a * l
rendimento = area / 2
print(f'O total de área para pintar são: {area :.2f}m2')
print(f'A quantia de tinta necessária é de: {rendimento :.2f} Litros')
print('Para cada 2 metros é usado 1 Litro de tinta por demão')