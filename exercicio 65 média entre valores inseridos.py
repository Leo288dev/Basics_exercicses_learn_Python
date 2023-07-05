#Exercício Python 65: Crie um programa que 1.leia vários números inteiros
# pelo teclado. No final da execução, 2.mostre a média entre todos os valores
# e 3.qual foi o maior e o menor valores lidos. O 4.programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
maior = menor = cont = numero = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))  # 1. ok
    numero += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    resp = str(input('Quer continuar ? S/N: ')).upper() .strip()[0]

print(f'A Some  é {numero} / {cont} =  a média entre eles = ',(numero / cont)) #2. media ok
print(f' O maior número inserido é :{maior}') 
print(f'O menor número inserido é : {menor}')




