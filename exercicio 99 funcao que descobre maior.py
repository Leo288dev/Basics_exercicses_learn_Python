#Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def valores(*num):
    tam = len(num)
    maior = 0
    for p, v in enumerate(num):
         if v > maior:
             maior = v
    print('-' * 30)
    print(f'Recebi ao todo {tam} números os valores são {num}')
    print(f'O maior valor inserido foi {maior}')
    print('-' * 30)


# PROGRAMA PRINCIPAL
valores(1, 3, 5, 4, 7, 3)
valores(3, 8, 5)
valores(0, 9)
valores(1, 6)
valores(0)
