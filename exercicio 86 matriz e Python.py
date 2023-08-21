# matriz1 = [[], [], []]
# matriz2 = [[], [], []]
# matriz3 = [[], [], []]
# for c in range(0, 9):
#     n = int(input(f'Digite o valor da {c + 1}º Matriz: '))
#     if c == 0:
#         matriz1[0].append(n)
#     elif c == 1:
#         matriz1[1].append(n)
#     elif c == 2:
#         matriz1[2].append(n)
#     elif c == 3:
#         matriz2[0].append(n)
#     elif c == 4:
#         matriz2[1].append(n)
#     elif c == 5:
#         matriz2[2].append(n)
#     elif c == 6:
#         matriz3[0].append(n)
#     elif c == 7:
#         matriz3[1].append(n)
#     elif c == 8:
#         matriz3[2].append(n)
#
#
# print(matriz1)
# print(matriz2)
# print(matriz3)

#solução Guanabara------------------------------------------------------------------------------------------------------
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c] :^5}]', end='')
    print()
