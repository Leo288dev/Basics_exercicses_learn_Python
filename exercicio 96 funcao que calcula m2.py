def metros(a, b):
    m = a * b
    print(f'A metragem aferida de {a :.2f} e de {b :.2f} é no total {m :.2f} M²')
def cabecalho(txt):
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


# PROGRAMA PRINCIPAL
while True:
    cabecalho('CÁLCULO DE METRAGEM')
    a = float(input('Primeira metragem: '))
    b = float(input('Segunda metragem: '))
    metros(a, b)
    menu = str(input('Continuar [S/N]: ')).upper()[0]
    while menu not in 'SN':
        menu = str(input('Digite apenas [S/N]: ')).upper()[0]
    else:
        if menu == 'N':
            break
print('FIM DO PROGRAMA ....')