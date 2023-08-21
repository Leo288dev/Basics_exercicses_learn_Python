#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# [1] O programa vai ler o nome do jogador e quantas partidas ele jogou. -------------- [ok]
# [2] Depois vai ler a quantidade de gols feitos em cada partida. --------------------- [ok]
# [3] No final, tudo isso será guardado em um dicionário, ----------------------------- [ok]
# [4] incluindo o total de gols feitos durante o campeonato. -------------------------- [ok]

print('-=' * 20)
print('   == GERENCIADOR DE APROVEITAMENTO ==   ')
print('-=' * 20)
gerenciamento = dict()
gol = list()
totGols = 0
aprov = 0
nome = str(input('Nome do Jogador: '))
partidas = int(input('Partidas: '))
for g in range(partidas):
    gols = int(input(f'{g + 1}º Partida: '))
    gol.append(gols)
for p, v in enumerate(gol):
    totGols += v
aprov = (totGols / partidas) * 100

gerenciamento['nome'] = nome
gerenciamento['partidas'] = partidas
gerenciamento['gols'] = gol
gerenciamento['totalGols'] = totGols
gerenciamento['aproveitamento'] = aprov

print()
print('-=' * 30)
print('-=' * 30)
print(' ==> DADOS ESTATÍSTICOS DO JOGADOR <==')
print('=-' * 30)
print(gerenciamento)
print('-=' * 30)
print(f'O campo nome tem o valor de {gerenciamento["nome"]}')
print(f'O campo gols tem o valor de: {gerenciamento["gols"]}')
print(f'O Campo total tem o valor de: {gerenciamento["totalGols"]}')
print('-=' * 30)
print(f'O jogador {gerenciamento["nome"]} jogou {gerenciamento["partidas"]} partidas.')
for i, z in enumerate(gol):
    print(f' => Na partida {i + 1}º, fez {z} gols')
print(f'Total de {gerenciamento["totalGols"]} gols')
print('=-' * 30)
print(f'Jogador {nome}Total de gols: {totGols}')
print(f'APROVEITAMENTO TOTAL: {aprov :.2f} %')
print('-=' * 30)
print('FIM...')
