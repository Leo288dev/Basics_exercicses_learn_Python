#Exercício Python 73: Crie uma tupla preenchida com
# os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#a) Os 5 primeiros times.    ------------------------ok
#b) Os últimos 4 colocados. -------------------------ok
#c) Times em ordem alfabética. ----------------------ok
#d) Em que posição está o time da Chapecoense. ------ok

tabela = ('Atlético Mineiro','Flamengo','Palmeiras','Fortaleza','Corinthians','Red Bull Bragantino','Fluminense',
          'America','Atlético','Santos','Ceará','Internacional','São Paulo','Athletico Paranaense ','Cuiabá',
          'Juventude','Grêmio','Bahia','Sport','Chapecoense')
print('-' * 70)
for t in tabela:
    print(t)
print('-' * 70)
print(f'Os cinco primeiros colocados na tabela do campeonato brasileiro são :'
      f'\n 1º {tabela[0]},\n '
      f'2º {tabela[1]},\n '
      f'3º {tabela[2]},\n '
      f'4º {tabela[3]},\n '
      f'5º {tabela[4]}.')
print('-' * 70)
print(f'Os Quatro últimos colocados são:\n {tabela[-4: ]}')
print('-' * 70)
print(f'Os times em ordem alfabética são:\n {sorted(tabela)}')
print('-' * 70)

for pos, time in enumerate(tabela):
        if time == 'Chapecoense':
            print(f'{time} está na {pos +1 }º posição do campeonato brasileiro')
print('-' * 70)