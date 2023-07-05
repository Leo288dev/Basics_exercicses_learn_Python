#Crie um programa que leia a idade e o sexo de
# várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

# print('-' * 30)
# print('BANCO DE DADOS')
# print('-' * 30)
# maior18 = 0
# homem = 0
# mulheresmenor20 = 0
# continuar = ''
# while True:
#     idade = int(input('Idade: '))
#     sexo = str(input('SEXO: [M/F]')).upper().strip()[0]
#     if idade >= 18:
#         maior18 += 1
#     if sexo == 'M':
#         homem += 1
#     if sexo == 'F' and idade < 20:
#         mulheresmenor20 += 1
#     print('-' * 30)
#     continuar = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
#     print('-' * 30)
#     if continuar == 'N':
#         break
# print(f'Foram cadastrados {maior18}  pessoas maiores de 18 anos')
# print(f'Foram cadastrados {homem} pessoas do sexo masculino')
# print(f'Foram cadastradas {mulheresmenor20} mulheres menores de 20 anos')

#_________RESOLUÇÃO DO GUANABARA-------------------

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper() .strip() [0]
    if resp == 'N':
         break
print('Acabou')
print(f'Total de pessoas com mais de dezoito anos: {tot18}')
print(f'Ao total temos {totH} homens cadastrados')
print(f'E temos {totM20} mulher(es) com menos de 20 anos')

