#Exercício Python 12: Faça um algoritmo que leia o preço
# de um produto e mostre seu novo preço, com 5%
# de desconto.

preco = float(input('Insira o preço: R$  '))
acrescimo = preco * 0.05
valor_final = preco - acrescimo
print('-' * 60)
print('PREÇO COM DESCONTO !!!')
print('-' * 60)
print('-' * 60)
print(f'O preçe de: R$ {preco :.2f} com DESCONTO de 5% R$ {acrescimo :.2f}')
print(f'Preço final de R$ {valor_final :.2f}')
print('-' * 60)