#Exercício Python 7: Desenvolva um programa
# que leia as duas notas de um aluno, calcule e
# mostre a sua média.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n2 + n1) / 2
print(f'Sua nota {n1 :.1f} somado com {n2 :.1f}')
print(f'Lhe concedeu a média {media :.1f}')