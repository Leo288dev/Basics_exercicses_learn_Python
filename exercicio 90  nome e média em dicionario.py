#Exercício Python 090: Faça um programa que leia nome e média de um aluno, ----------------- (ok)
# guardando também a situação em um dicionário. -------------------------------------------- (ok)
# No final, mostre o conteúdo da estrutura na tela. ---------------------------------------- (ok)
principal = []
aluno = {}
while True:
    aluno['name'] = str(input('Nome do aluno: '))
    aluno['media'] = float(input('Média do aluno: '))
    if aluno['media'] < 6:
        aluno['Situação'] = 'Reprovado(a)'
    else:
        aluno['Situação'] = 'Aprovado(a)'
    principal.append(aluno.copy())

    menu = str(input('Deseja incluir mais alunos ?  [S/N]: ')).upper()
    if menu in 'N':
        break
    else:
        if menu not in 'SN':
            menu = str(input('Deseja continuar? Somente[S/N]: ')).upper()

for c in principal:
    print(f'O aluno(a): {c["name"]} consta como: {c["Situação"]} sua média foi: {c["media"]:.2f}')
