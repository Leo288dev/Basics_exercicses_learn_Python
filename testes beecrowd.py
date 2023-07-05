

#beecrowd 1001-----------EXTREMAMENTE BÁSICO-----------------
# a = int(input(''))
# b = int(input(''))
# x = a + b
# print(f'X = {x}')

#beecrowd 1102---------ÁREA DO CÍRCULO----------------------
#fórmula para calculo de área area = n.raio2
# raio = float(input(''))
# n = 3.14159
# area = n*(raio**2)
# print(f'A={area:.4f}')

#beecrowd 1003 ----------SOMA SIMPLES ------------------

# a = int(input(''))
# b = int(input(''))
# soma = a + b
# print(f'SOMA = {soma}')

#beecrowd 1004 -------PRODUTO SIMPLES----------------
# a = int(input(''))
# b = int(input(''))
# PROD = a * b
# print(f'PROD = {PROD}')

#beecrowd 1005 ----------MEDIA PONDERADA---------------
# a = float(input(''))
# b = float(input(''))
# mediaA =3.5 * a
# mediaB = 7.5 * b
# pesos = 3.5 + 7.5
# ponderada = (mediaA + mediaB) / pesos
# print(f'MEDIA = {ponderada :.5f}')

#BEECROWD 1006 ---------MEIDA 2------------------------
# A = float(input(''))
# B = float(input(''))
# C = float(input(''))
# mediaA = 2 * A
# mediab = 3 * B
# mediac = 5 * C
# pesos = 2 + 3 + 5
# mediaFinal = (mediaA + mediab + mediac) / pesos
# print(f'MEDIA = {mediaFinal :.1f}')

#-------BEECROWD 1007 ----------------------------

# A = int(input(''))
# B = int(input(''))
# C = int(input(''))
# D = int(input(''))
# diferenca = A * B - C * D
# print(f'DIFERENCA = {diferenca}')

#== BEECROWD 1008 --------------------------------

# number = int(input(''))
# hours = int(input(''))
# valH = float(input(''))
# salary = hours * valH
# print(f'NUMBER = {number}')
# print(f'SALARY = U$ {salary :.2f}')

# BEECROWD 1009 ----------------------------------

# name = str(input(''))
# salary = float(input(''))
# sales_amount = float(input(''))
# commission = 0.15 * sales_amount + salary
# print(f'TOTAL = R$ {commission :.2f}')

#----BEECROWD 1010 -------------------------------------

#LIST1

# n = input('')
# values = n.split()
# if len(values) != 3:
#     print('Please enter three values')
# else:
#     valor0 = int(values[0])
#     valor1 = int(values[1])
#     valor2 = float(values[2])
# lista1 = [valor0, valor1, valor2]
#
# #LIST2
#
# n2 = input('')
# values2 = n2.split()
# if len(values2) != 3:
#     print('Please enter three values')
# else:
#     valor00 = int(values2[0])
#     valor11 = int(values2[1])
#     valor22 = float(values2[2])
# lista2 = [valor00, valor11, valor22]
#
# value_to_be_paid = valor1 * valor2 + valor11 * valor22
# print(f'VALOR A PAGAR: R$ {value_to_be_paid :.2f}')

#BEECROWD 1011 --------------------------------------------------------------------
#calculo de esfera fórmula (R) raio
# (4/3) * pi * R3 valor do pi 3.14159
#dica (4/3.0) ou (4/0*3)


# R = int(input(''))
# calc = (4/3) * 3.14159 * R**3
# print(f'VOLUME = {calc :.3f}')

#BEECROWD 1112 -----------------------------------------------

e = input('')
param = e.split()
a = float(param[0])
b = float(param[1])
c = float(param[2])
triangle = (a * c) / 2
circle = c ** 2 * 3.14159
trapezio = (a + b) / 2 * c
square = b ** 2
rectangle = a * b
print(f'TRIANGULO: {triangle :.3f}')
print(f'CIRCULO: {circle :.3f}')
print(f'TRAPEZIO: {trapezio :.3f}')
print(f'QUADRADO: {square :.3f}')
print(f'RETANGULO: {rectangle :.3f}')
