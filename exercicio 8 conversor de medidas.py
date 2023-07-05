#Exercício Python 8: Escreva um programa que
# leia um valor em metros e o exiba convertido
# em centímetros e milímetros.

medida = float(input('Insira a medida: '))
conversor_deca = medida * 10
conversor_cm = medida * 100
conversor_mm = medida * 1000
conversor_km = medida / 1000

print(f'Sua media em Kilometros é: {conversor_km}')
print(f'Sua medida em decametro é: {conversor_deca :.2f}dc')
print(f'Sua media em centímetros é: {conversor_cm :.2f}cm')
print(f'Sua medida em milímetros é: {conversor_mm :.2f}mm')