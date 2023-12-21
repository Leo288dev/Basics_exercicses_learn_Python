#Exercício Python 100: Faça um programa que tenha
# [1] uma lista chamada números -----------------------------------------------------------------------[ok]
# [2] e duas funções chamadas sorteia() e somaPar(). --------------------------------------------------[ok]
# [3] A primeira função vai sortear 5 números e vai colocá-los dentro da lista ------------------------[ok]
# [4] e a segunda função vai mostrar a soma entre todos os valores pares ------------------------------[ok]
# sorteados pela função anterior.
# from random import randint
#
# numeros_aleatorios = []
#
#
# def sorteia(qtd, valor_minimo, valor_maximo):
#     for _ in range(5):
#         numero_aleatorio = randint(valor_minimo, valor_maximo)
#         numeros_aleatorios.append(numero_aleatorio)
#
#     return(numeros_aleatorios)
#
# def somapar(num):
#     soma = 0
#     for p, v in enumerate(números):
#         if v % 2 == 0:
#             soma += v
#     return soma
#
# #PROGRAMA PRINCIPAL
#
# números = sorteia(5, 1, 10)
# s0ma = somapar(números)
#
# print(f'Os números sorteados foram: {números}')
# print(f'A soma dos pares é: {s0ma}')
#
#
##====================================================
##============= RESOLUÇÃO GUANABARA ==================
##====================================================

from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO !!!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando so valores pares da lista {lista} temos {soma}')

#PROGRAMA PRINCIPAL

números = list()
sorteia(números)
somaPar(números)
