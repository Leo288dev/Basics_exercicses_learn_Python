#Exercício Python 18: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

a = int(input('Insira o angulo: '))
radianos = radians(a)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f'O Seno do ângulo {a} é: {seno :.2f} ')
print(f'O Cosseno do ângulo {a} é: {cosseno :.2f}')
print(f'A Tangente do ângulo {a} é: {tangente :.2f}')
print(f' O ângulo {a} convertido em radianos é: {radianos}')