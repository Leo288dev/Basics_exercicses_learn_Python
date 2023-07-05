#Exercício Python 55: Faça um programa que leia o peso de cinco
# pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesoMaior = 0
pesoMenor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: '))
    if p == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso

print(f'A Pessoa com Maior peso tem {pesoMaior :.2f}Kg.')
print(f'A Pessoa com Menor peso tem {pesoMenor :.2f}Kg.')
