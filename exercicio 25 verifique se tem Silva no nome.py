#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela
# tem “SILVA” no nome.

nome = input('Digite seu nome: ') .title() .strip() .title()
nome1 = nome, 'Silva' in nome
print('=' * 60)
print(f'Possui Silva no nome ? {nome1}')
print('-' * 30)
print('Legenda')
print('True == Sim')
print('False == Não')
print('-' * 30)





