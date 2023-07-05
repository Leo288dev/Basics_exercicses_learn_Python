#Exercício Python 30: Crie um programa que leia um número inteiro e
# mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Insira um número pra seber se ele é par ou ímpar: '))
if n % 2 == 0:
    print(f'O número {n} é par !!!!')
else:
    print(f'O número {n} é ímpar !!!')