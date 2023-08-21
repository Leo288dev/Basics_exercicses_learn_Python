#Exercício Python 089: Crie um programa que
# leia nome e duas notas de vários alunos (ok)
# e guarde tudo em uma lista composta. (ok)
# No final, mostre um boletim contendo a média de cada um ()
# e permita que o usuário possa mostrar as notas de cada aluno individualmente. ()
lista = list()

while True:
    n = str(input('Insira o nome do Aluno: '))
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1 + n2) / 2
    lista.append([n, [n1, n2], media])

    menu = str(input('Deseja continuar ?: [S/N]')).upper()
    if menu not in "SN":
        print('Favor digitar apenas [S] ou [N]: ')
        menu = str(input('Deseja continuar ?: [S/N]')).upper()
    else:
        if menu in "N":
            break

print('=' * 21)
print('ESCOLA PILAR DO SABER')
print('=' * 21)
print('______ Boletim ______')
print(f'{"Nº" :<4}{"Nome" :<10}{"Média":>8}')
for i, a in enumerate(lista):
    print(f'{i :<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas detalhadas ? (999 ENCERRA): '))
    if opc == 999:
        break

    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são: {lista[opc][1]}')
