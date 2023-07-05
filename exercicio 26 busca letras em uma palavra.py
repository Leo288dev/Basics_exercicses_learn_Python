#Exercício Python 26: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra “A”, em que posição ela aparece
# a primeira vez e em que posição ela aparece a última vez.

busca = str(input('Insira uma palavra: '))
palavra = busca .strip() .upper()
print('-' * 30)
palavra1 = palavra.count('A')
palavra2 = palavra.find('A')
palavra3 = palavra.rfind('A')
print('-' * 30)
print('Análise PARAFRASEAL')
print('-' * 30)

print(f'Analisando a palavra {busca.upper()} temos; ')
print(f'* A letra aparece {palavra1} vezes !!!')
print(f'* A letra aparece a primeira vez na posição: {palavra2}')
print(f'A letra A aparece a última vez na posição: {palavra3}')
