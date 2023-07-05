# Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi
# o maior e o menor valor digitado e as suas respectivas
# posições na lista.
posmaior = ''
posmenor = ''
maior = ''
menor = ''
lista = []
for c in range(1, 6):
    l = int(input(f'digite {c}ºvalor: '))
    maior = l
    menor = l
    lista.append(l)
for i, v in enumerate(lista):
    if v > maior:
        maior = v
        posmaior = i
    if v < menor:
        menor = v
        posmenor = i
print('-' * 30)
print(f'A lista digitada foi: {lista}')
print('-' * 30)
print(f'O maior valor da lista foi: {maior} e está na posição {posmaior}')
print('-' * 30)
print(f'O menor valor da lista foi: {menor} e está na posição {posmenor}')








