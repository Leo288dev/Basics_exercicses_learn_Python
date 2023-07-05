#Exercício Python 66: Crie um programa que 1.leia números inteiros pelo
# teclado. 2.O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, 3.mostre quantos números foram digitados
# 4.e qual foi a soma entre elas (desconsiderando o flag).

# n = int(input('Insira um número inteiro [999 Encerra]: '))
# cont = soma = 0
#
# while n != 999:
#     soma += n
#     cont += 1
#     n = int(input('Insira um número inteiro [999 Encerra]: '))
# print(f'O total de números digitados foi {cont}')
# print(f'A soma entre estes números é: {soma}')

#======================================================
# SOLUÇÃO GUANABARA - USANDO BREAK
cont = soma = 0
while True:
    n = int(input('Digite um num. [999 encerra]: '))
    if n == 999:   # cont e soma é colocado depois do if para não somar o 999
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números e a soma deles é: {soma}')
