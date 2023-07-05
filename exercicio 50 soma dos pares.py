#Exercício Python 50: Desenvolva um programa que leia seis números
# inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

print('~|~' * 10)
print('{:^30}'.format ('SOMA PARES'))
print('~|~' * 10)
par = 0
cont = 0
for pares in range(1,7):
    num = int(input(f'Insira o {pares} número: '))
    if num % 2 == 0:
        par = par + num
        cont = cont + 1
print(f'Você informou {cont} números pares e a soma deles é {par}')
