#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes


print('=-' * 30)
print('ANALISADOR DE TRIÂNGULOS')
print('=-' * 30)

a = float(input('Insira o primeiro segmento BASE: '))
b = float(input('Insira o segundo segmento LADO: '))
c = float(input('Insira o terceiro segmento LADO: '))

if b + c > a:
    print('Estes segmentos juntos FORMAM UM TRIÂNGULO')
    if b == c and b == a and c == b and c == a:             #EQUIÁTERO
        print('Este triângulo é um EQUILÁTERO')
    elif b == c and b != a and c == b and c != a:           # ISÓCELES
        print('Este triângulo é um ISÓCELES')
    elif b != c and b != a and c != b and c != a:           #ESCALENO
        print('Este triângulo é um ESCALENO')
else:
    print('Estes segmentos juntos NÃO FORMAM UM TRIÂNGULO')

