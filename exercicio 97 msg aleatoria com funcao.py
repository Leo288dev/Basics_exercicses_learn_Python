#Exercício Python 097: Faça um programa que tenha uma função chamada
# escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.

# def texto(txt):
#     print('-' * len(txt))
#     print(f'{txt :.^10}')
#     print('-' * len(txt))
#
#
# t = str(input('Digite a mensagem: '))
# texto(t)
#
# v = str(input('Digite a segunda mensagem: '))
# texto(v)
#
# z = str(input('Digite a terceira mensagem: '))
# texto(z)

from datetime import datetime

def diaAtual():
  return datetime.now().strftime("%m/%d/%Y")


a = diaAtual()
print(a)

