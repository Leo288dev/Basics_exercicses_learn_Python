#Exercício Python 27: Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente

nome = str(input('Insira o nome completo: ')) .strip() .upper()
print(f'Olá {nome}, Tudo bem ? ')
n = nome .split()
print('Primeiro nome:',n[0])
print(f'Ultimo nome: {n[len(n)-1]}')


