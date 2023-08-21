#Exercício Python 088: Faça um programa que ajude um jogador da
# MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e -------------------------------------ok
# vai sortear 6 números entre 1 e 60 para cada jogo, -----------------------------------------ok
# cadastrando tudo em uma lista composta.            -----------------------------------------ok
from random import randint
palpites = []
n = 0
rodadas = int(input('Digite quantos palpites quer: '))
print('=' * 33)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('=' * 33)
for c in range(rodadas):
    lista = []
    while len(lista) < 6:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            lista.sort()
    palpites.append(lista)
    print(f'Sorteio {c +1}: {palpites[c]} ')

print('===========< BOA SORTE >===========')







