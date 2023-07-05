#Exercício Python 15: Escreva um programa que pergunte a quantidade
# de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

km_rodados = float(input('Insira a km rodada: '))
dias = int(input('Insira os dias alugados: '))
totalDias = dias * 60
totalKm = km_rodados * 0.15
totalAluguel = totalKm + totalDias
print(f'Foram {dias} dias alugados em um total de: R${totalDias :.2f}')
print(f'Foram rodados {km_rodados :.2f} km, Total de: R${totalKm :.2f}')
print(f'O valor total do aluguel  dias e km rodados é: R${totalAluguel :.2f}')