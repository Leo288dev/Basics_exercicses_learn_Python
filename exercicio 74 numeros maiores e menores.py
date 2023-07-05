#Exercício Python 074: Crie um programa que vai
# 1.gerar cinco números aleatórios e colocar em uma tupla. ------------------------ ok
# Depois disso, mostre
# 2. a listagem de números gerados -------------------------------------------------ok
# e também indique
# 3. o menor e o maior valor que estão na tupla.

from random import randint

sorteio = tuple(randint(1, 10) for _ in range(5))
print(sorteio)
menor_valor = min(sorteio)
maior_valor = max(sorteio)
print(f'O Menor valor contido no sorteio é: {menor_valor}')
print(f'O maior valor contido no sorteio é : {maior_valor}')





