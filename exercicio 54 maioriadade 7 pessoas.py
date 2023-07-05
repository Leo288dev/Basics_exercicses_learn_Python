# Exercício Python 54: Crie um programa que leia o ano de
# nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
anoAtual = int(ano)
contMaior = 0
contMenor = 0
for i in range(1, 8):
    pessoas = int(input(f'Em que ano a {i} pessoa nasceu ?  '))
    idade = anoAtual - pessoas
    if idade > 21:
        contMaior += 1
    else:
        contMenor += 1

print(f'Temos {contMaior} pessoas Maior(es) de Idade')
print(f'E também temos {contMenor} pessoa Menor(es) de Idade ')










