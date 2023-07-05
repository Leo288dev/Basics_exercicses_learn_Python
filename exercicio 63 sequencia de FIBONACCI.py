#Exercício Python 63: Escreva um programa que leia um número
# N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('=' * 20)
print('SEQUÊNCIA DE FIBONACCI')
print('=' * 20)
n = int(input('Quantos termos vc quer ? : '))
t1 = 0
t2 = 1
t3 = t1 + t2
cont = 3            # contador inicia em 3 pq já possui os dois primeiros termos da sequência
print('~' * 20)
print(f'{t1} - {t2} -', end='')
while cont <= n:
    t3 = t1 + t2
    print(f' {t3} - ', end='')
    t1 = t2     # desloca os valores fazendo que o cálculo passe a ser o antecessor e o último termo
    t2 = t3     #   idem a acima
    cont += 1
print('END')
print('~' * 20)