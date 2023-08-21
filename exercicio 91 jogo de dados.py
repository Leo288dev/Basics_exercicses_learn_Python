#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
dic = {'Jogador 1': randint(1, 6),
       'Jogador 2': randint(1, 6),
       'Jogador 3': randint(1, 6),
       'Jogador 4': randint(1, 6)}
ranking = list()
print('== LANCES DA RODADA ==')
for c, v in dic.items():
    print(f'O {c} tirou {v}')
    sleep(1)


ranking = sorted(dic.items(), key = itemgetter(1), reverse=True)
print('-=' * 20)
print(' == RANKING DOS GANHADORES == ')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
print()


print('Fim da execução')
#


