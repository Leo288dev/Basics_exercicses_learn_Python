#Exercício Python 077: Crie um programa que tenha
# uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

palavras = ('Aprender', 'Python', 'Programacao', 'Tecnologia', 'Saber', 'Computador', 'Furico')
for p in (palavras):
    print(f'\nA palavra {p.upper()} tem as vogais: ', end='')
    for letras in (p):
        if letras.lower() in'aeoiu':
            print(letras, end=' ')


