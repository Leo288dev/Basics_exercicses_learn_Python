#Exercício Python 040: Crie um programa que leia duas notas de um
# aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:

nota1 = float(input('Digite a primeira nota: '))
while nota1 > 10 or nota1 <0:
    nota1 = float(input('Favor digitar um valor entre 0 e 10: '))
nota2 = float(input('Digite a segunda nota: '))
while nota2 > 10 or nota1 <0:
    nota2 = float(input('Favor digitar um valor entre 0 e 10: '))


media = (nota1 + nota2) / 2
print(f'Sua média é:{media}')

if media < 5:
    print('Aluno Reprovado')
elif media  > 5 and media < 7:
    print('Talvez com Recuperação')
elif media >= 7:
    print('Aluno Aprovado')
