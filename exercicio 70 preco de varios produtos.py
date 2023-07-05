#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.


print('-' * 40)
print('Lojas Baratão')
print('-' * 40)
preco = mil = MaisBarato = 0
NomeBarato = 'p'


while True:
    p = str(input('Nome do Produto: '))
    n = float(input('Valor do produto:R$ '))
    preco += n
    continuar = str(input('Continuar a compra ? :  ')) .upper().strip()[0]
    if continuar == 'N':
        print('')
        print('=-' * 15)
        print('Programa encerrado')
        print('')
        break

    if n > 1000:
        mil += 1

    if n < 1000 and MaisBarato < n:
        MaisBarato = n
        NomeBarato = p


print('=' * 30)
print(f'Total da compra foi R${preco :.2f}')
print(f'{mil} Produto(s) com preço acima de R$1.000')
print(f'O produto mais barato é : {NomeBarato} e custa R${MaisBarato :.2f}')
print('=' * 30)

#-------SOLUÇÃO GUANABARA -------------------
# total = totmil = cont = 0
# barato = ' '
# while True:
#     produto = str(input('Nome do Produto: '))
#     preco = float(input('Preço R$ '))
#     total += preco
#     if preco > 1000:
#         totmil += 1
#     if cont == 1:
#         menor = preco
#         barato = produto
#     else:
#         if preco < menor:
#             menor = preco
#
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar? ')).upper().strip()[0]
#     if resp == 'N':
#         break
# print('{:-^40}'.format((' FIM DO PROGRAMA ')))
# print((f'O total da compra foi{total :.2f}'))
# print(f'Temos {totmil} produtos custando mais de R$10000')
# print(f'O produto mais barato é {barato} e custa {menor} ')
