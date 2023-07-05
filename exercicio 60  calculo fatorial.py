#Exercício Python 060: Faça um programa que leia um número qualquer e
# mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
# n = int(input('Insira um número: '))
# c = n
# f = 1
# while c > 0:
#     print(f'{c}' , end='')
#     print('x' if c > 1 else '=', end='')
#     f *= c
#     c-= 1
# print(f'{f}')


#----------- USANDO FOR ----------------------------------------------------
n = int(input('Insira um número: '))
c = n
f = 1
print(f'Calculando o Fatorial de {n}!')
print(n, end='x')
while c > 1:
    for i in range(n-1, 0, -1):
        print(i, end='')
        print('x' if c > 2 else '=', end='')
        f *= c
        c -= 1
print(f'{f}')
