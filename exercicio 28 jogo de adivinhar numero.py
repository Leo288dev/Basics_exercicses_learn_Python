#Exercício Python 28: Escreva um programa que faça o computador
# “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-=' * 60)
print(' ### JOGO DE ADIVINHAR ###')
print('-=' * 60)
n = int(input('Adivinhe um numero  entre 0 e 5  e insira ele aqui: '))
numero = randint(0,5)

if n > 5 or n < 0:
    print('Digite um valor entre ZERO E CINCO !!! ')
    n = int(input('Adivinhe um numero  entre 0 e 5  e insira ele aqui: '.strip()))
print('Processando ......')
sleep(3)
if n == numero:
     print('Caramba vc é bom mesmo acertou !!!!')
else:
    print('Xiiii, vc errou !!!')

