#Exercício Python 038: Escreva um programa que leia dois números inteiros
# e compare-os. mostrando na tela uma mensagem:
print('-' * 40)
print('COMPARADOR DE VALORES')
print('-' * 40)
print('')
n = int(input('Insira o primeiro valor: '))
m = int(input('Insira o segundo valor : '))

if n > m:
    print(f'O Primeiro valor {n} é MAIOR')
elif m > n:
    print(f'O segundo valor {m} é MAIOR')
else:
    print(f' NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS')
    