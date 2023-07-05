#Exercício Python 14: Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.
t = float(input('Insira a tempretaura em Celsius: '))
conversor = t * 9 / 5 + 32
fahrenheit = conversor
print(f'A temperatura {t :.2f} Celsius')
print(f'é  equivalente à {fahrenheit :.2f} Fahrenheit')

# a formula de conversão celsius fahrenheit é {...}   * 9 / 5 + 32
#                                               |     |-----------|
#                                               |           |
#                                               |    Fórmula de conversão
#                                               |
#                                           Temp. Celsius