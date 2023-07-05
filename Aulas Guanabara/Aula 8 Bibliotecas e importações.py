#Exercício Python 16: Crie um programa que leia um número Real
# qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import ceil, trunc
n = float(input('Digite um valor: '))
inteiro = trunc(n)
print (f'O valor digitado foi {n} e sua porção inteira foi: {inteiro}')