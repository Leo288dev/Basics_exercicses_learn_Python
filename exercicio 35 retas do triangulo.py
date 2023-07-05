#Exercício Python 35: Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Para formar triangulos cada dois lados devem ser sempre maiores
#que a medida do terceiro lado. FÓRMULA: b + c > a
print('=-' * 30)
print('ANALISADOR DE TRIÂNGULOS')
print('=-' * 30)

a = float(input('Insira o primeiro segmento: '))
b = float(input('Insira o segundo segmento: '))
c = float(input('Insira o terceiro segmento: '))

if b + c > a:
    print('Estes segmentos juntos FORMAM UM TRIÂNGULO')
else:
    print('Estes segmentos juntos NÃO FORMAM UM TRIÂNGULO')

