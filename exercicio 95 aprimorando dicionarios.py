#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# [1] O programa vai ler o nome do jogador e quantas partidas ele jogou. -------------- [ok]
# [2] Depois vai ler a quantidade de gols feitos em cada partida. --------------------- [ok]
# [3] No final, tudo isso será guardado em um dicionário, ----------------------------- [ok]
# [4] incluindo o total de gols feitos durante o campeonato. -------------------------- [ok]

#Exercício Python 095:
# [1] Aprimore o desafio 93 para que ele funcione com vários jogadores, -------------------------[ok]
# [2] incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.--------[]
time = list()

while True:
    totalGols = 0
    jogador = {}
    gols = []
    nome = str(input('Nome: '))
    partidas = int(input('Partidas Jogadas: '))
    for g in range(partidas):
        gols.append(int(input(f'{g + 1}º Partidas: ')))
    jogador['nome'] = nome
    jogador['partidas'] = partidas
    jogador['gols'] = gols
    for p, v in enumerate(gols):
        totalGols += v
    jogador['totalGols'] = totalGols
    time.append(jogador)
    del(jogador)
#---------------------------------------- MENU CONTINUAR --------------------------------------------------------------
    menu = str(input('Deseja continuar ?  [S / N]: ')).upper()[0]
    while menu not in 'SN':
        print('ERRO!!! Digitar apenas S ou N')
        menu = str(input('Deseja continuar ?  [S / N]: ')).upper()[0]
    if menu in 'N':
        break
#----------------------------------------------------------------------------------------------------------------------
print('=-' * 30)
print('LISTA COMPLETA DOS JOGADORES')
print('-=' * 30)
print(time)
print()
#----------------------------------------------------------------------------------------------------------------------

print('-=' * 30)
print('VISÃO DETALHADA')
print('-=' * 30)
print()
while True:
    for f, e in enumerate(time):
        print(f'{[f]} {e["nome"]} \n')

    detalhe = int(input('digite a opção para ter os dados do jogador [999 ENCERRA ]: '))
    if detalhe == 999:
       print('===< PROGRAMA ENCERRADO >===')
       break


    else:
        if detalhe == f:
            print('=' * 30)
            print(f'JOGADOR: {e["nome"]} possui os resultados: ')
            print('-_-' * 10)
            print(f'PARTIDAS DISPUTADAS:  {e["partidas"]}')
            print(f'GOLS REALIZADOS TOTAL: {e["totalGols"]}')
            for i, z in enumerate(time[0]['gols']):
                print(f'{i + 1}º Partida margou {z} gols')
            print('-_-' * 10)


