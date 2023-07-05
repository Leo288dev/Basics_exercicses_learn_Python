#Exercício Python 52: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num = int(input('Digite um número para saber se é primo: '))
tot = 0
for c in range(1,num +1):
    if num % c == 0:
        print('\033[33m', end='') #código para inseriri cores
        tot = tot + 1
    else:
        print('\033[31m',end='') #código para inserir cores
    print(f'{c}', end ='')
print(f'\n \033[mO {num} foi divisível {tot} Vezes !!!') # código que trona default a cor em branco

