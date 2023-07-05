#Exercício Python 64: Crie um programa que leia vários números inteiros
# pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = int(input('Digite um numero inteiro{DIGITE 999 PARA PARAR]: '))
cont = 0
numeros = 0
while n != 999:
    numeros += n
    cont += 1
    n = int(input('Digite um numero inteiro: '))

print(f'A soma total é {numeros} com {cont} iterações')


