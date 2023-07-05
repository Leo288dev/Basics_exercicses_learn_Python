#Exercício Python 33: Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o segundo número: '))

#Bloco do número maior
print('-' * 30)
if a > b and a > c:
    print(f'O maior número é: {a}')

elif b > a and b > c:
    print(f'O maior numero é: {b}')

else:
    print (f'O maior número é: {c}')
print('-' * 30)

# Bloco do número menor

if a < b and a < c:
    print(f'O menor número é: {a}')

elif b < a and b < c:
    print(f'O menor número é {b}')

else:
    print(f'O menor número é: {c}')
print('-' * 30)
