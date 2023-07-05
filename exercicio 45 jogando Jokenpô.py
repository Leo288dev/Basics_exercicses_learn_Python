#Exercício Python 45: Crie um programa que faça o computador
# jogar Jokenpô com você.
import random
from random import randint
from time import sleep

itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('-' * 30)
print('{:^30}'.format ('JOKENPÔ')) # 30 espaços vazios centralizando o jokenpo
print('-' * 30)
print('{:=^28}'.format(' MENU ')) # 30 sinais de igual centralizando menu
print(' [0] PEDRA \n '
    '[1] PAPEL\n '
      '[2] TESOURA')
jogador = int(input('Qual é a sua jogada ? '))
print('')
print('JO'), sleep(1)
print('KEN'), sleep(1)
print('PÔ !!!!!'),sleep(1)
print('-=' * 15)
print(f'O jogador escolheu {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
print('-=' * 15)

#--------------------Pedra-----------------------
if jogador == 0 and computador == 1:
    print ('O jogador perdeu a rodada !!!')
elif jogador == 0 and computador == 0:
    print('Rodada empatada !!!')
elif jogador == 0 and computador == 2:
    print ('Jogador venceu a Rodada !!!')

#------------------Papel____________________________
elif jogador == 1 and computador == 0:
    print('Jogador venceu a rodada !!!')
elif jogador == 1 and computador == 1:
    print('Rodada empadata')
elif jogador == 1 and computador == 2:
    print('Computador venceu a Rodada !!!')

#------------------Tesoura--------------------------
elif jogador == 2 and computador == 0:
    print ('Computador venceu a Rodada !!!')
elif jogador == 2 and computador == 1:
    print('Jogador venceu a Rodada !!!')
elif jogador == 2 and computador == 2:
    print('Rodada empatada !!!')
print('')