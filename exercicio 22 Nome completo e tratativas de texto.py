#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = str(input('Insira seu nome copmleto:'))
nome1 = nome.upper()
nome2 = nome.lower()
nome3 = nome.strip()
nome4 = nome.split()
print(f'Seu nome em letra MAIÚSCULA é: {nome1}')
print(f'Seu nome em letra MINÚSCULA é: {nome2}')
print(f'Seu nome sem espaços tem {len(nome3)} letras')
print(f'Seu primeiro nome é {nome4[0]} tem {len(nome4[0])} letras')