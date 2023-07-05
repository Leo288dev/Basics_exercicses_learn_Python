#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
Lista = [[], []]
for n in range(0, 7):
    N = int(input(f'Digite o {n+1}º número: '))
    if N % 2 == 0:
        Lista[0].append(N)
    else:
        Lista[1].append(N)

Lista[0].sort()
Lista[1].sort()
print('-=' * 30)
print(f'Os Numeros pares digitados foram: {Lista[0]}')
print(f'Os Números ímpares digitados foram: {Lista[1]}')
