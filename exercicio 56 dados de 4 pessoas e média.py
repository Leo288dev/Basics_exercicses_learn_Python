#Exercício Python 56: Desenvolva um programa que leia o nome, idade
# e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.
anos  = 0
maisVelho = 0
nomeMaisvelho = ''
contFem = 0
for p in range(1, 7):
    print(f'-' * 15, f'{p}ªpessoa', '-' * 15)
    nome = str(input(f'Insira o nome da {p}ª pessoa: ') .upper().strip())
    idade = int(input(f'Insira a idade da {p}ª pessoa: '))
    sexo = int(input(f'Insira o sexo da {p}ª pessoa [1]Feminino ou [2]Masculino: '))
    anos += idade

    if sexo == 2:
        if p == 1:
            maisVelho = idade
            nomeMaisvelho = nome
        else:
            if idade > maisVelho:
                maisVelho = idade
                nomeMaisvelho = nome



    if sexo == 1:
        if idade < 20:
            contFem += 1

    print('=' * 40)


print(f' Todas as idades somam {anos} e a média de idade do grupo  é : {anos / p :.0f} anos')
print(f'O nome do Homem mais velho do grupo é: {nomeMaisvelho}')
print(f'No grupo possui {contFem} mulher(es) com idade abaixo 20 anos ')


#------------SOLUÇÃO GUANABARA-------------------------------------------------------------
# somaidade = 0
# mediaidade = 0
# maioridadehomem = 0
# nomevelho = 0
# totmulher20 = 0
# for p in range(1, 5):
#     print(f'-------{p}ªPESSOA--------')
#     nome = str(input('nome:')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('SEXO M/F: ')).strip()
#     somaidade += idade
#     if p == 1 and sexo in 'Mm':
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Mm' and idade > maioridadehomem:
#         maioridadehomem = idade
#     if sexo in 'Ff' and idade < 20:
#         totmulher20 += 1
# mediaidade = somaidade / 4
# print(f'A média de idade dp grupo é {mediaidade} anos ')
# print(f'O homem mais velho do grupo se chama: {nomevelho}')
# print(f'Ao todo são {totmulher20} com menos de 20 anos')