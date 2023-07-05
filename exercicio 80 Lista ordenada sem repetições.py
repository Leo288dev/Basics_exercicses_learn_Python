#Crie um programa onde o usuário possa digitar ------------------------------------------------ok
# cinco valores numéricos ---------------------------------------------------------------------ok
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela. ------------------------------------------------- ok

lista = list()
for c in range(0,5):
    n = int(input('Insira o valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Valor inserido na última posição')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1
print(lista)



