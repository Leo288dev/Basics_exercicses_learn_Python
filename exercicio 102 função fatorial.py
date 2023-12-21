#Crie um programa que tenha
# uma função fatorial()que receba dois parâmetros:
# o primeiro que indique o número a calcular e
# outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# def fatorial(n, show=False):
#     """
#     -> Calcula o fatorial de um número
#     :param n: Número que será fatorado
#     :param show: Mostra a conta ou não
#     :return: o valor do cálculo
#     """
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' X', end=' ')
#             else:
#                 print('=', end=' ')
#         f *= c
#     return f
#
#
# print(fatorial(5, show=True))
# print(help(fatorial))
#


#PRATICANDO O EXERCÍCIO FATORIAL


def fatorial(n, Show=False):
    f = 1
    for c in range(n, 0, -1):
        if Show == True:
            print(c, end=' ')
            if c > 1:
                print(' X ', end=' ')
            else:
                print(' = ', end='')
        f *= c
    return f



print(fatorial(5))
