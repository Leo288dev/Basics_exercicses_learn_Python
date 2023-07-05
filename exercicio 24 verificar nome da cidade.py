#Exercício Python 24: Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome “SANTO”.

cid = input('Digite o nome da cidade: ') .capitalize() .strip()
cid1 = cid, 'Santo' in cid
print('-' * 30)
print('Legenda')
print(' True == Sim')
print('False == Não')
print('-' * 30)
print(f' A cidade digitada possui Santo no nome: {cid1}')
