#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a
# ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada.

from random import shuffle
a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)

print(f'A ordem de apresentação será: {alunos}')
