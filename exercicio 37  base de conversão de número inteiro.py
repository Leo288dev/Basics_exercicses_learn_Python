#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Insira um numero inteiro: '))

print('1 - BINÁRIO \n'
      '2 - OCTAL\n'
      '3 - EXADECIMAL')

menu = int(input('Digite a base para realizar a conversão: '))

binario = bin(n)
octa = oct(n)
hexadecimal = hex(n)

if menu == 1:
    print(f'O número: {n} convertido para Binário é: {binario[2:]}')
elif menu == 2:
    print(f'O número: {n} convertido para Octal é: {octa [2:]}')
elif menu ==3:
    print(f'O número: {n} convertido para Hexadecimal é: {hexadecimal[2:]}')
else:
    print('Opção errada, digite novamente')