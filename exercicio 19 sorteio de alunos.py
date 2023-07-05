#Exercício Python 19: Um professor quer sortear um dos seus quatro
# alunos para apagar o quadro. Faça um programa que ajude ele, lendo
# o nome dos alunos e escrevendo na tela o nome do escolhido.

# MEU MÉTODO DE RESOLUÇÃO DO PROBLEMA
import random

alunos = ['Maria', 'João', 'Pedro', 'Augusto']
sorteio = random.randint(0, 3)
if sorteio == 0:
    print('Maria foi a sorteada !!!')

elif sorteio == 1:
    print('João foi o sorteado !!!')

elif sorteio == 2:
    print('Pedro foi o sorteado !!!')

else:
    print('Augusto foi o sorteado !!!')



#____________________________________________________________________
# MÉTODO DO GUANABARA

# from random import choice
#
# n1 = input('Primeiro aluno: ')
# n2 = input('Segundo aluno: ')
# n3 = input('Terceiro aluno: ')
# n4 = input('Quarto aluno: ')
#
# alunos = [n1,n2,n3,n4]
#
# sorteio = choice(alunos)
#
# print(f'O aluno sorteado foi: {sorteio}')