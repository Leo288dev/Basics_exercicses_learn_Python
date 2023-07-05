#Exercício Python 17: Faça um programa que leia o comprimento do
# cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

# print('-' * 60)
# print('Fazendo o cálculo do Triângulo Retângulo sem uso de biblioteca')
# print('-' * 60)

#hipotenusa = float(input('Insira a hipotenusa: '))
# cat_oposto = float(input('Insira o cateto oposto: '))
# cat_adjacente = float(input('Insira o cateto adjacente: '))
#
# #hipo = hipotenusa ** 2
# oposto = cat_oposto ** 2
# adja = cat_adjacente ** 2
#
# resultado = oposto + adja
# hipotenusa_tot = resultado ** 0.5
# print(f'As medidas são: \n '
#       f'Adjacente {adja:.0f}; \n'
#       f' oposto: {oposto:.0f}; \n ')
#       #f'Hipotenusa {hipo:.0f}.')
# print(f'A soma dos catetos é: {resultado:.0f} portanto a hipotenusa é: {hipotenusa_tot:.2f}')

#------------------------------------------------------------------------------------------------------
print('-' * 60)
print('Usando a bliblioteca MATH função hypot')
print('-' * 60)

cat_oposto = float(input('Insira o cateto oposto: '))
cat_adjacente = float(input('Insira o cateto adjacente: '))

hipotenusa = hypot(cat_oposto,cat_adjacente)
print(f'O valor da Hipotenusa é:{hipotenusa :.2f}')
